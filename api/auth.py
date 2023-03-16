from datetime import datetime, timedelta
from os import getenv

from dotenv import load_dotenv
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import SecretStr
from sqlalchemy.orm import Session

from api.crud.users_crud import (
    get_user_by_email,
    get_user_by_id,
    insert_user,
    update_user_password,
)
from db.setup import get_db
from schema.token_schema import Token, TokenData
from schema.users_schema import User, UserIn, UserInDB

load_dotenv()

SECRET_KEY = str(getenv("SECRET_KEY"))
assert SECRET_KEY is not None

ALGORITHM = str(getenv("ALGORITHM"))
assert ALGORITHM is not None

_ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
assert _ACCESS_TOKEN_EXPIRE_MINUTES is not None

ACCESS_TOKEN_EXPIRE_MINUTES = int(_ACCESS_TOKEN_EXPIRE_MINUTES)
ACCESS_TOKEN_EXPIRE_TIMEDELTA = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(tags=["auth"])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, email: str):
    if email in db:
        user_dict = db[email]
        return UserInDB(**user_dict)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_id_sub_access_token(user_id: int):
    return {
        "access_token": create_access_token(
            data={"sub": str(user_id)}, expires_delta=ACCESS_TOKEN_EXPIRE_TIMEDELTA
        ),
        "token_type": "bearer",
    }


async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        raw_sub = payload.get("sub")
        if raw_sub is None:
            raise credentials_exception
        user_id: int = int(raw_sub)
        token_data = TokenData(user_id=user_id)
    except JWTError as exc:
        raise credentials_exception from exc
    # user = get_user_by_email(db, email=token_data.email)
    if token_data.user_id is None:
        raise credentials_exception
    user = get_user_by_id(db, id=token_data.user_id)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user),
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> Token:
    # note that form_data only accepts username and password fields as per OAuth2 standard
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return create_id_sub_access_token(user.id)


@router.post("/register")
def register_user(new_user: UserIn = Body(), db: Session = Depends(get_db)) -> Token:
    hashed_password = get_password_hash(new_user.password.get_secret_value())
    user = insert_user(db, UserInDB(**new_user.dict(), hashed_password=hashed_password))

    return create_id_sub_access_token(user.id)


# TODO: require password confirmation
@router.put("/password")
def reset_password(
    new_password: SecretStr = Body(),
    active_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    new_password_hash = get_password_hash(new_password.get_secret_value())
    update_user_password(db, int(active_user.id), new_password_hash)
    return {"message": "Password updated."}

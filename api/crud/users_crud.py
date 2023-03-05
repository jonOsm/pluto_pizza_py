from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from schema.users_schema import UserInDB, User
from db.models import UserModel 


def insert_user(db: Session, user_in: UserInDB) -> User:
    integrity_exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Email already assocaited with an account.",
    )
    try:
        db.add(UserModel(**user_in.dict()))
        db.commit()
        
        return get_user_by_email(db, user_in.email)
    except IntegrityError as e:
        raise integrity_exception


def get_user_by_email(db: Session, email: str, include_addresses: bool = True) -> User:
    #TODO: Determine if there are any errors we should catch here.
    query = select(UserModel).where(UserModel.email == email)
    return db.scalar(query)

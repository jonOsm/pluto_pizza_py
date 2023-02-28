from fastapi import HTTPException, status
from schema.users import UserInDB
from sqlalchemy.orm import Session
from db.models import User
from sqlalchemy.exc import IntegrityError


def insert_user(db: Session, user_in: UserInDB):
    integrity_exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Email already assocaited with an account.",
    )
    try:
        db.add(User(**user_in.dict()))
        db.commit()
    except IntegrityError as e:
        raise integrity_exception

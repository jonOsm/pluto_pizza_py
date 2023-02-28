from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from schema.users import UserInDB
from db.models import User


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


def get_user_by_email(db: Session, email: str):
    query = select(User).where(User.email == email)
    return db.scalar(query)

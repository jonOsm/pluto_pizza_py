from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from schema import users
from db import models


def insert_user(db: Session, user_in: users.UserInDB) -> users.User:
    integrity_exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Email already assocaited with an account.",
    )
    try:
        db.add(models.User(**user_in.dict()))
        db.commit()
        
        return get_user_by_email(db, user_in.email)
    except IntegrityError as e:
        raise integrity_exception


def get_user_by_email(db: Session, email: str) -> users.User:
    #TODO: Determine if there are any errors we should catch here.
    query = select(models.User).where(models.User.email == email)
    return db.scalar(query)

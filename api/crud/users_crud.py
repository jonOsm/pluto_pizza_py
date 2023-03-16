from fastapi import HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from schema.users_schema import UserDetails, UserInDB
from db.models import UserModel


def insert_user(db: Session, user_in: UserInDB):
    integrity_exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail={
            "msg": "Email already assocaited with an account.",
            "type": "custom.duplicate",
        },
    )
    try:
        db.add(UserModel(**user_in.dict()))
        db.commit()

        return get_user_by_email(db, user_in.email)
    except IntegrityError:
        raise integrity_exception


def get_user_by_email(db: Session, email: str):
    # TODO: Determine if there are any errors we should catch here.
    # TODO: Determine best practices for filtering data
    query = select(UserModel).where(UserModel.email == email)
    return db.scalar(query)


def get_user_by_id(db: Session, id: int):
    # TODO: Determine if there are any errors we should catch here.
    # TODO: Determine best practices for filtering data
    query = select(UserModel).where(UserModel.id == id)
    return db.scalar(query)


def db_update_user_details(db: Session, user_id: int, user_details: UserDetails):
    stmt = (
        update(UserModel).where(UserModel.id == user_id).values(**user_details.dict())
    )
    db.execute(stmt)
    db.commit()
    return get_user_by_email(db, user_details.email)


def update_user_password(db: Session, user_id: int, hashed_password: str) -> None:
    stmt = (
        update(UserModel)
        .where(UserModel.id == user_id)
        .values(hashed_password=hashed_password)
    )
    db.execute(stmt)
    db.commit()


def delete_user(db: Session, user_id: int):
    user = db.get(UserModel, user_id)
    db.delete(user)
    db.commit()

    return user

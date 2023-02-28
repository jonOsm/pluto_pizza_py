from schema.users import UserInDB
from sqlalchemy.orm import Session
from db.models import User


def insert_user(db: Session, user_in: UserInDB):
    db.add(User(**user_in.dict()))
    db.commit()

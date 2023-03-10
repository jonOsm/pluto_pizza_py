from fastapi import APIRouter, Body, Depends
from api.crud.users_crud import db_update_user_details
from db.setup import get_db
from sqlalchemy.orm import Session

from schema.users_schema import User, UserDetails
from api.auth import get_current_active_user


router = APIRouter(prefix="/users", tags=["users"])


@router.put("/profile")
def modify_user_details(
    new_details: UserDetails = Body(),
    active_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> User:
    return db_update_user_details(db, active_user.id, new_details)


@router.get("/active")
def show_current_user(
    current_user: User = Depends(get_current_active_user),
) -> User:
    return current_user

from fastapi import APIRouter, Depends
from api.crud.users_crud import db_update_user_details, delete_user
from db.setup import get_db
from sqlalchemy.orm import Session

from schema.users_schema import User, UserDelete, UserDetails
from api.auth import get_current_active_user


router = APIRouter(prefix="/users", tags=["users"])


@router.put("/profile")
def modify_user_details(
    new_details: UserDetails,
    active_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> User:
    return db_update_user_details(db, int(active_user.id), new_details)


@router.get("/active")
def show_current_user(
    current_user: User = Depends(get_current_active_user),
) -> User:
    return current_user


@router.delete("/profile")
def destroy_user(
    active_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> UserDelete:
    return delete_user(db, int(active_user.id))

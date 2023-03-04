from fastapi import APIRouter

from schema.users_schema import User, UserIn


router = APIRouter(prefix="/users")

#todo
from enum import Enum

from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from schema.users import User, UserIn


class UserFilters(str, Enum):
    admin = ("admin",)
    basic = "basic"


class Product(BaseModel):
    name: str


router = APIRouter(prefix="/users")


# # create user
# @router.post("/", response_model=UserOut)
# async def create_user(user: UserIn) -> User:
#     # return specified user
#     pass


# read user?


# @router.get("/{id}")
# async def get_user(id: int) -> list[Product]:
#     # return specified user
#     pass


# @router.get("/")
# async def get_all_users() -> list[Product]:
#     # return all users
#     pass


# update user
# delete user

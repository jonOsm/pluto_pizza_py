from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel

from schema.users import UserIn


class Product(BaseModel):
    name: str


router = APIRouter(prefix="/products")


@router.get("/")
async def read_all_products() -> list[Product]:
    pass


# create user
@router.post("/user/")
async def read_all_products(id: UserIn) -> list[Product]:
    # return specified user
    pass


# read user?


@router.get("/user/{id}")
async def read_all_products(id: int) -> list[Product]:
    # return specified user
    pass


@router.get("/user")
async def read_all_products() -> list[Product]:
    # return all users
    pass


# update user
# delete user

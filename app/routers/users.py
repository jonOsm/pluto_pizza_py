from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel

class UserFilters(str, Enum):
    admin='admin',
    basic='basic'

class BaseUser(BaseModel):
    name:str

router = APIRouter(
    prefix="/users"
)

@router.get("/filter/{user_filter}")
async def get_users(user_filter: UserFilters | None = None) -> list[BaseUser]:
    return [BaseUser(name='Frank'), BaseUser(name='Anne')]

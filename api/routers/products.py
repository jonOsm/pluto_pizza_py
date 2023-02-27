from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel

class Product(BaseModel):
    name:str

router = APIRouter(
    prefix="/products"
)

@router.get("/")
async def read_all_products() -> list[Product]:
    return [Product(name='Pepperoni Pizza'), Product(name='Deluxe Pizza')]

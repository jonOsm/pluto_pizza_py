from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.products_schema import Product
from api.crud.products_crud import read_products
from fastapi_pagination import Page
from db.setup import get_db

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
async def index(db: Session = Depends(get_db)) -> Page[Product]:
    return read_products(db)

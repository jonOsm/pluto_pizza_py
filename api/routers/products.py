from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.products_schema import Product
from api.crud.products_crud import read_all_products 
from db.setup import get_db 

router = APIRouter(prefix="/products", tags=['products'])

@router.get("/")
async def products_index(db:Session =  Depends(get_db)) -> list[Product]:
    return read_all_products(db)
    

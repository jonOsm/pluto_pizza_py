from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.products_schema import Product
from api.db_utils.product import get_all_products 
from db.setup import get_db 

router = APIRouter(prefix="/products", tags=['products'])

@router.get("/")
async def read_all_products(db:Session =  Depends(get_db)) -> list[Product]:
    return get_all_products(db)
    

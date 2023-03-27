from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.products_schema import Product
from schema.product_customization_schema import ProductCustomizationDefault
from api.crud.products_crud import read_products
from api.crud.product_customizations_crud import read_product_customization
from fastapi_pagination import Page
from db.setup import get_db

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
async def index(db: Session = Depends(get_db)) -> Page[Product]:
    return read_products(db)


@router.get("/{product_id}/customization/default")
async def default_product_customization(
    product_id: int, db: Session = Depends(get_db)
) -> ProductCustomizationDefault:
    return read_product_customization(db, product_id)

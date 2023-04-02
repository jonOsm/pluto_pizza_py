from fastapi import APIRouter, Depends
from fastapi_pagination import paginate
from sqlalchemy.orm import Session
from schema.products_schema import Product, ProductWithEssentialCustomization
from schema.product_customization_schema import (
    ProductCustomizationDefault,
    ProductCustomizationOptions,
)

from api.crud.products_crud import read_products
from api.crud.product_customizations_crud import (
    read_default_product_customization,
    read_product_customization_options,
)
from fastapi_pagination import Page
from db.setup import get_db

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
async def index(
    db: Session = Depends(get_db),
) -> Page[ProductWithEssentialCustomization]:
    return paginate(read_products(db))


@router.get("/{product_id}/customization/default")
async def default_product_customization(
    product_id: int, db: Session = Depends(get_db)
) -> ProductCustomizationDefault:
    prod_cust_record = read_default_product_customization(db, product_id)
    toppings = [
        topping_record.topping for topping_record in prod_cust_record.toppings
    ]
    del prod_cust_record.toppings
    return ProductCustomizationDefault(
        **prod_cust_record.__dict__, toppings=toppings
    )


@router.get("/customization/options")
async def get_product_customization_options(
    db: Session = Depends(get_db),
) -> ProductCustomizationOptions:
    return read_product_customization_options(db)

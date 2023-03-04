from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import ProductModel 
from schema.products_schema import Product 

def read_all_products(db: Session) -> list[Product]: 
    stmt = select(ProductModel)
    return db.scalars(stmt).all()

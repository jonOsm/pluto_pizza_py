from sqlalchemy import select
from sqlalchemy.orm import Session

from db import models
from schema import products_schema

def get_all_products(db: Session): 
    stmt = select(models.Product)
    products = db.scalars(stmt).all()
    return db.scalars(stmt).all()

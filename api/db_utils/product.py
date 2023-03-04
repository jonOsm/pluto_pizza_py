from sqlalchemy import select
from sqlalchemy.orm import Session

from db import models
from schema import products_schema

def get_all_products(db: Session) -> list[products_schema.Product]: 
    stmt = select(models.Product)
    return db.scalars(stmt).all()

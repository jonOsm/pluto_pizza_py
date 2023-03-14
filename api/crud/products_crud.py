from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import ProductModel


def read_all_products(db: Session):
    stmt = select(ProductModel)
    return db.scalars(stmt).all()

from sqlalchemy import select
from sqlalchemy.orm import Session
from db.models import ProductModel
from fastapi_pagination.ext.sqlalchemy_future import paginate


def read_products(db: Session):
    stmt = select(ProductModel).order_by(ProductModel.created_at)
    # return db.scalars(stmt).all()
    return paginate(db, stmt)

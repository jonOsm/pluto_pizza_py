from sqlalchemy import select, desc, alias
from sqlalchemy.orm import Session
from db.models import ProductCustomizationsModel, ProductModel, ProductSizeModel
from fastapi_pagination.ext.sqlalchemy_future import paginate


def read_products(db: Session):
    stmt = (
        select(ProductModel, ProductSizeModel.name.label("product_size_name"))
        .join_from(ProductModel, ProductCustomizationsModel)
        .join_from(ProductCustomizationsModel, ProductSizeModel)
        .where(ProductCustomizationsModel.is_default)
        .order_by(ProductModel.created_at)
    )
    print(stmt)

    a = db.scalars(stmt)
    b = db.scalars(stmt).all()
    return b
    return db.scalars(stmt).all()
    # return paginate(db, stmt)

from sqlalchemy import select, desc, alias
from sqlalchemy.orm import Session
from db.models import ProductCustomizationsModel, ProductModel, ProductSizeModel

from fastapi_pagination.ext.sqlalchemy_future import paginate


def read_products(db: Session):
    stmt = (
        select(ProductModel, ProductSizeModel)
        .join_from(ProductModel, ProductCustomizationsModel)
        .join_from(ProductCustomizationsModel, ProductSizeModel)
        .where(ProductCustomizationsModel.is_default)
        .order_by(ProductModel.created_at)
    )
    print(stmt)
    products = [
        {**row.ProductModel.__dict__, "product_size": row.ProductSizeModel}
        for row in db.execute(stmt).all()
    ]
    return products
    # return paginate(db, stmt)

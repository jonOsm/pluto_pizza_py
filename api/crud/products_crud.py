from sqlalchemy import select
from sqlalchemy.orm import Session
from db.models import ProductCustomizationsModel, ProductModel, ProductSizeModel


def read_products(db: Session):
    stmt = (
        select(ProductModel, ProductSizeModel)
        .join_from(ProductModel, ProductCustomizationsModel)
        .join_from(ProductCustomizationsModel, ProductSizeModel)
        .where(ProductCustomizationsModel.is_default)
        .order_by(ProductModel.created_at)
    )
    return [
        {**row.ProductModel.__dict__, "product_size": row.ProductSizeModel}
        for row in db.execute(stmt).all()
    ]

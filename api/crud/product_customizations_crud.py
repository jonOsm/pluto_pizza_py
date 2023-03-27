from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import ProductCustomizationsModel


def read_all_secondary_customization(db: Session, model: any):
    stmt = select(model)

    return db.scalars(stmt).all()


def read_product_customization(
    db: Session, product_id: int, defaults_only: bool = True
):
    base_stmt = select(ProductCustomizationsModel).where(
        ProductCustomizationsModel.product_id == product_id
    )

    if defaults_only:
        base_stmt = base_stmt.where(ProductCustomizationsModel.is_default == True)

    return db.scalars(base_stmt).first()

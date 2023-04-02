from typing import Sequence
from db.models import ProductCustomizationToppingsModel, ToppingModel, ToppingTypeModel
from sqlalchemy import select
from sqlalchemy.orm import Session


def read_toppings(
    db: Session, topping_types: None | list[str] = None
) -> Sequence[ToppingModel]:
    if topping_types:
        stmt = (
            select(ToppingModel)
            .join(ToppingModel.topping_type)
            .where(ToppingTypeModel.name.in_(topping_types))
        )
    else:
        stmt = select(ToppingModel)
    print(stmt)
    return db.scalars(stmt).all()


def read_unselected_toppings(db: Session, product_customization_id: int):
    stmt = (
        select(ToppingModel)
        .join(ProductCustomizationToppingsModel)
        .where(
            ProductCustomizationToppingsModel.product_customization_id
            != product_customization_id
        )
    )
    return db.scalars(stmt).all()

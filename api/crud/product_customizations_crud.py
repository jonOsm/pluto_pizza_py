from sqlalchemy import select
from sqlalchemy.orm import Session
from api.crud.toppings_crud import read_toppings

from db.models import (
    ProductCustomizationsModel,
    CrustTypeModel,
    CrustThicknessModel,
    CheeseAmtModel,
    CheeseTypeModel,
    SauceAmtModel,
    SauceTypeModel,
)


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


def read_product_customization_options(db: Session):
    customization_option_models = {
        "crust_type": CrustTypeModel,
        "crust_thickness": CrustThicknessModel,
        "cheese_amt": CheeseAmtModel,
        "cheese_type": CheeseTypeModel,
        "sauce_amt": SauceAmtModel,
        "sauce_type": SauceTypeModel,
    }

    customization_option_values = {
        option: read_all_secondary_customization(db, model)
        for (option, model) in customization_option_models.items()
    }

    customization_option_values["toppings"] = read_toppings(db)
    return customization_option_values

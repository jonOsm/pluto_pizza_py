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
    ProductSizeModel,
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
        base_stmt = base_stmt.where(
            ProductCustomizationsModel.is_default == True
        )

    return db.scalars(base_stmt).first()


def read_product_customization_options(db: Session):
    customization_option_models = {
        "crust_type": CrustTypeModel,
        "crust_thickness": CrustThicknessModel,
        "cheese_amt": CheeseAmtModel,
        "cheese_type": CheeseTypeModel,
        "sauce_amt": SauceAmtModel,
        "sauce_type": SauceTypeModel,
        "product_size": ProductSizeModel,
    }

    customization_option_values = {
        option: read_all_secondary_customization(db, model)
        for (option, model) in customization_option_models.items()
    }

    # TODO: Consideration - fragile implementation
    # if the user adds a new topping type, it won't be included unless we update the list below
    # also, doing two queries when we could filter here instead
    customization_option_values["toppings"] = read_toppings(
        db, ["vegetables", "meat"]
    )
    customization_option_values["additional_toppings"] = read_toppings(
        db, ["other"]
    )
    return customization_option_values

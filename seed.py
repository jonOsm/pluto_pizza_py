from sqlalchemy import and_, delete, func, select, update
from sqlalchemy.orm import Session
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import get_db
from db.models import (
    CheeseAmtModel,
    CheeseTypeModel,
    CrustThicknessModel,
    CrustTypeModel,
    ProductCustomizationToppingsModel,
    ProductCustomizationsModel,
    ProductModel,
    SauceAmtModel,
    SauceTypeModel,
    ProductSizeModel,
    ToppingModel,
    ToppingTypeModel,
    UserModel,
)


def delete_all_records(session, models):
    print("Resetting DB...")
    for model in models:
        session.execute(delete(model))
    session.commit()
    print("Resetting DB done.\n")


def gen_entity(factory: SQLAlchemyModelFactory, qty: int, label: str) -> None:
    print(f"Seeding {label}...")
    factory.create_batch(qty)
    print(f"Seeding {label} done.\n")


def seed_topping_types(session):
    print("Seeding ToppingTypes...")
    toppingTypes = [
        ToppingTypeModel(name="vegetables"),
        ToppingTypeModel(name="meat"),
        ToppingTypeModel(name="other"),
    ]
    session.add_all(toppingTypes)
    session.commit()
    print("Seeding ToppingTypes done.")
    return toppingTypes


def seed_toppings(session: Session, toppingTypes: list[ToppingTypeModel]):
    vegetable_id = topping_types[0].id
    meat_id = topping_types[1].id
    other_id = topping_types[2].id

    toppings = [
        ToppingModel(name="tomatoes", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="green peppers", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="red peppers", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="onions", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="chives", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="arugula", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="mushrooms", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="broccoli", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="cauliflower", base_price=1.99, type_id=vegetable_id),
        ToppingModel(name="pepperoni", base_price=1.99, type_id=meat_id),
        ToppingModel(name="chicken", base_price=3.99, type_id=meat_id),
        ToppingModel(name="bacon crumble", base_price=1.99, type_id=meat_id),
        ToppingModel(name="bacon strips", base_price=3.99, type_id=meat_id),
        ToppingModel(name="sausage", base_price=1.99, type_id=meat_id),
        ToppingModel(name="olive oil", base_price=0, type_id=other_id),
        ToppingModel(name="sriracha", base_price=0, type_id=other_id),
        ToppingModel(name="frank's red hot", base_price=0, type_id=other_id),
    ]
    session.add_all(toppings)
    session.commit()


def seed_name_only(session: Session, model, names: list[str]):
    entities = [model(name=n) for n in names]
    session.add_all(entities)
    session.commit()


def set_default_customizations(session: Session):
    subquery = (
        select(
            ProductCustomizationsModel.product_id,
            func.max(ProductCustomizationsModel.created_at).label("max_created_at"),
        )
        .group_by(ProductCustomizationsModel.product_id)
        .subquery()
    )
    stmt = select(ProductCustomizationsModel).join_from(
        ProductCustomizationsModel,
        subquery,
        and_(
            ProductCustomizationsModel.product_id == subquery.c.get("product_id"),
            ProductCustomizationsModel.created_at == subquery.c.get("max_created_at"),
        ),
    )
    default_customizations = session.scalars(stmt).all()
    update_dict = [{"id": pc.id, "is_default": True} for pc in default_customizations]
    session.execute(
        update(ProductCustomizationsModel),
        update_dict,
    )
    session.commit()


if __name__ == "__main__":
    print("Seeding DB...")
    # WARNING: Order matters! Not all deletions cascade.
    # TODO: Drop and recreate all tables instead?
    models = [
        UserModel,
        ProductCustomizationToppingsModel,
        ProductCustomizationsModel,
        CrustTypeModel,
        CrustThicknessModel,
        CheeseTypeModel,
        SauceTypeModel,
        SauceAmtModel,
        CheeseAmtModel,
        ToppingModel,
        ProductSizeModel,
        ToppingTypeModel,
        ProductModel,
    ]
    session: Session = next(get_db())

    delete_all_records(session, models)

    topping_types = seed_topping_types(session)
    seed_toppings(session, topping_types)

    seed_name_only(session, CrustTypeModel, ["white", "whole grain", "keto-friendly"])
    seed_name_only(session, CrustThicknessModel, ["thin", "normal", "thick"])
    seed_name_only(session, CheeseTypeModel, ["mozzarella", "four cheese blend"])
    seed_name_only(session, SauceTypeModel, ["classic tomato", "pesto", "bbq"])
    seed_name_only(session, SauceAmtModel, ["less", "normal", "extra"])

    session.add_all(
        [
            ProductSizeModel(name="small", base_price=8.99),
            ProductSizeModel(name="medium", base_price=9.99),
            ProductSizeModel(name="large", base_price=10.99),
            ProductSizeModel(name="xl", base_price=13.99),
            ProductSizeModel(name="party", base_price=15.99),
        ]
    )

    session.add_all(
        [
            CheeseAmtModel(name="less", base_price=0),
            CheeseAmtModel(name="normal", base_price=0),
            CheeseAmtModel(name="extra", base_price="2.99"),
        ]
    )
    session.commit()

    from db.factories.user_factory import UserFactory
    from db.factories.product_factory import ProductFactory

    gen_entity(UserFactory, 50, "Users")
    gen_entity(ProductFactory, 50, "Products")
    set_default_customizations(session)
    print("Seeding DB complete.")

    session.close()

from sqlalchemy import delete
from sqlalchemy.orm import Session
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import get_db
from db.factories.user_factory import UserFactory, UserModel
from db.factories.product_factory import ProductFactory, ProductModel
from db.models import ToppingModel, ToppingTypeModel


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


if __name__ == "__main__":
    print("Seeding DB...")
    models = [UserModel, ProductModel, ToppingModel, ToppingTypeModel]
    session: Session = next(get_db())

    delete_all_records(session, models)

    topping_types = seed_topping_types(session)
    seed_toppings(session, topping_types)
    gen_entity(UserFactory, 50, "Users")
    gen_entity(ProductFactory, 50, "Products")

    print("Seeding DB complete.")

    session.close()


from sqlalchemy import delete
from sqlalchemy.orm import Session
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import get_db
from db.factories.user_factory import UserFactory, UserModel 
from db.factories.product_factory import ProductFactory, ProductModel

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

if __name__ == "__main__":
    print("Seeding DB...")
    models = [UserModel, ProductModel]
    session: Session = next(get_db())

    delete_all_records(session, models)

    gen_entity(UserFactory, 50, 'Users')
    gen_entity(ProductFactory, 50, 'Products')

    print("Seeding DB complete.")



from sqlalchemy import delete
from sqlalchemy.orm import Session
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import get_db
# from db.models import UserModel, ProductModel
from db.factories.user_factory import UserFactory, UserModel
from db.factories.product_factory import ProductFactory, ProductModel
from db.factories.address_factory import AddressFactory , AddressModel

def gen_entity(factory: SQLAlchemyModelFactory, qty: int, label: str) -> None:
    print(f"Seeding {label}.") 
    factory.create_batch(qty)
    print(f"Seeding {label} done.\n")

if __name__ == "__main__":
    # reset db
    print("Resetting DB.")
    session: Session = next(get_db())
    # stmt = delete(UserModel)
    # session.execute(stmt)
    # session.commit()

    stmt = delete(ProductModel)
    session.execute(stmt)
    session.commit()
    print("Resetting DB done.\n")

    AddressFactory.create_batch(50)
    # gen_entity(UserFactory, 50, 'Users')
    # gen_entity(ProductFactory, 50, 'Products')
    # gen_entity(AddressFactory, 50, 'Addresses')
    print("Seeding done.")
    print("Seeding DB complete.")


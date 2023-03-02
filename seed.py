from db.factories.user_factory import UserFactory
from db.factories.product_factory import ProductFactory
from sqlalchemy import delete
from sqlalchemy.orm import Session
from db.setup import get_db
from db.models import User

if __name__ == "__main__":
    # reset db
    print("Resetting DB...")
    session: Session = next(get_db())
    stmt = delete(User)
    session.execute(stmt)
    session.commit()
    print("Resetting DB: DONE")

    # seed
    print("Seeding DB...")
    print("Seeding Users...")
    UserFactory.create_batch(50)
    print("Seeding Users: Done")
    print("Seeding DB: DONE")

    print("Seeding Users...")
    ProductFactory.create_batch(50)
    print("Seeding Users: Done")

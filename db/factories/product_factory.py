from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import get_scoped_session
from db.models import User, Product


class ProductFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = get_scoped_session()
        sqlalchemy_session_persistence = "commit"

    name = Faker("sentence", nb_words=2)
    base_price = Faker("random_number", digits=4)
    base_size = Faker(
        "random_elements", elements=["small", "medium", "large", "xl", "party"]
    )
    is_draft = Faker("boolean", chance_of_getting_true=10)
    stock = Faker("random_number", digits=2)
    sku = Faker("uuid4")
    image_url = "todo"

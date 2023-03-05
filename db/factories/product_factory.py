from factory import Faker, LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import scoped_session_local 
from db.models import UserModel, ProductModel


class ProductFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ProductModel
        exclude = ["_name_base", "_price_base"]
        sqlalchemy_session = scoped_session_local 
        sqlalchemy_session_persistence = "commit"
    
    _name_base = Faker("words", nb=2)
    _price_base = Faker("random_number", digits=4)

    name = LazyAttribute(lambda p: f"{' '.join(p._name_base)} pizza")
    base_price = LazyAttribute(lambda p: p._price_base / 100)
    base_size = Faker(
        "random_element", elements=["small", "medium", "large", "xl", "party"]
    )
    is_draft = Faker("boolean", chance_of_getting_true=10)
    stock = Faker("random_number", digits=2)
    sku = Faker("uuid4")
    image_url = "todo"

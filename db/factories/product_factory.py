from factory import Faker, LazyAttribute, RelatedFactoryList
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import scoped_session_local
from db.models import ProductModel
from .product_customizations_factory import ProductCustomizationsFactory


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

    product_customizations = RelatedFactoryList(
        ProductCustomizationsFactory, "product", 10
    )

    is_draft = Faker("boolean", chance_of_getting_true=10)
    stock = Faker("random_number", digits=2)
    sku = Faker("uuid4")
    image_url = Faker(
        "random_element",
        elements=[
            "/static/img/products/pepperoni.jpg",
            "/static/img/products/mediterranean.jpg",
            "/static/img/products/arugula.jpg",
            "/static/img/products/cheese.jfif",
            "/static/img/products/hawaiian.webp",
        ],
    )

from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import scoped_session_local
from db.models import ProductCustomizationsModel
from db.pre_seed import (
    get_toppings,
    crust_types,
    crust_thicknesses,
    cheese_amts,
    cheese_types,
    sauce_amts,
    sauce_types,
    product_sizes,
)


class ProductCustomizationsFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ProductCustomizationsModel
        sqlalchemy_session = scoped_session_local
        sqlalchemy_session_persistence = "commit"

    crust_type_id = Faker("random_element", elements=[ct.id for ct in crust_types])
    crust_thickness_id = Faker(
        "random_element",
        elements=[ct.id for ct in crust_thicknesses],
    )
    cheese_type_id = Faker("random_element", elements=[ct.id for ct in cheese_types])
    cheese_amt_id = Faker("random_element", elements=[ca.id for ca in cheese_amts])
    sauce_type_id = Faker("random_element", elements=[st.id for st in sauce_types])
    sauce_amt_id = Faker("random_element", elements=[sa.id for sa in sauce_amts])
    product_size_id = Faker("random_element", elements=[ps.id for ps in product_sizes])
    toppings = Faker(
        "random_elements",
        elements=list(get_toppings(scoped_session_local)),
        unique=True,
    )

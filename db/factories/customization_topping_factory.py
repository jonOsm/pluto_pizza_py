from random import choice, choices, randint
from factory import Faker, LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import scoped_session_local
from db.models import ProductCustomizationToppingsModel
from db.pre_seed import get_toppings


class CustomizationToppingsFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ProductCustomizationToppingsModel
        sqlalchemy_session = scoped_session_local
        sqlalchemy_session_persistence = "commit"

    topping = LazyAttribute(lambda _: choice(get_toppings(scoped_session_local)))

    # crust_type_id = Faker("random_element", elements=[ct.id for ct in crust_types])
    # crust_thickness_id = Faker(
    #     "random_element",
    #     elements=[ct.id for ct in crust_thicknesses],
    # )
    # cheese_type_id = Faker("random_element", elements=[ct.id for ct in cheese_types])
    # cheese_amt_id = Faker("random_element", elements=[ca.id for ca in cheese_amts])
    # sauce_type_id = Faker("random_element", elements=[st.id for st in sauce_types])
    # sauce_amt_id = Faker("random_element", elements=[sa.id for sa in sauce_amts])
    # product_size_id = Faker("random_element", elements=[ps.id for ps in product_sizes])
    # # toppings = LazyAttribute(
    # #     lambda _: choices(list(get_toppings(scoped_session_local)), k=randint(0, 3))
    # # )
    # toppings = Faker(
    #     "random_elements",
    #     elements=list(get_toppings(scoped_session_local)),
    #     unique=True,
    # )

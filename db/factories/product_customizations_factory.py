from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import scoped_session_local
from db.models import ProductCustomizationsModel
from db.pre_seed import (
    toppings,
    crust_types,
    crust_thicknesses,
    cheese_amts,
    cheese_types,
    sauce_amts,
    sauce_types,
)


class ProductCustomizationsFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ProductCustomizationsModel
        exclude = ["_crusts"]
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
    toppings = Faker(
        "random_elements", elements=list(toppings(scoped_session_local)), unique=True
    )

    # @factory.post_generation
    # def toppings(obj, create, extracted, **kwargs):
    #     num_toppings = randint(0,6)
    #     random_toppings = choices(toppings, k=num_toppings)

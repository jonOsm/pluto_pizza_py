from factory import Faker, post_generation
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import scoped_session_local
from db.models import ProductCustomizationToppingsModel, ProductCustomizationsModel
from random import choices, randint
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

    @post_generation
    def generate_toppings(obj, create, extracted, **kwargs):
        toppings = get_toppings(scoped_session_local)
        chosen_toppings = set(choices(toppings, k=randint(1, len(toppings) // 3)))
        customization_toppings = [
            ProductCustomizationToppingsModel(
                topping_id=topping.id, product_customization_id=obj.id
            )
            for topping in chosen_toppings
        ]
        scoped_session_local.add_all(customization_toppings)
        scoped_session_local.commit()

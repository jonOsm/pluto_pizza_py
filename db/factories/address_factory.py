import datetime
from factory import Faker, LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory
import random
from db.setup import scoped_session_local
from db.models import AddressModel

# from .user_factory import UserFactory


def or_none(obj, none_probability: float = 0.5):
    if none_probability >= 1 or none_probability <= 0:
        raise ValueError("none_probability must be between 0 and 1 exclusive.")

    r_num = random.random()
    return None if r_num < none_probability else obj


class AddressFactory(SQLAlchemyModelFactory):
    class Meta:
        model = AddressModel
        exclude = ["_base_extension", "_base_label"]
        sqlalchemy_session = scoped_session_local
        sqlalchemy_session_persistence = "commit"

    _base_extension = Faker("random_number", digits=3)
    _base_label = Faker("words", nb=2)

    label = LazyAttribute(lambda a: or_none(" ".join(a._base_label)))
    street = Faker("street_name")
    unit = Faker("secondary_address")
    city = Faker("city")
    province = Faker("province", locale="en_CA")
    country = "Canada"
    postal_code = Faker("postalcode", locale="en_CA")
    phone_number = Faker("phone_number", locale="en_CA")
    extension = LazyAttribute(lambda a: or_none(a._base_extension))

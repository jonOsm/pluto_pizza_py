import datetime
from factory import Faker, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
import random
from db.setup import get_scoped_session
from db.models import AddressModel 
from .user_factory import UserFactory


class AddressFactory(SQLAlchemyModelFactory):
    class Meta:
        model = AddressModel 
        sqlalchemy_session = get_scoped_session() 
        sqlalchemy_session_persistence = "commit"


    user_id = 857 
    label = Faker('words', nb=2)
    street = Faker('street_name') 
    unit = Faker('secondary_address') 
    city = Faker('city')
    province = Faker('province', locale='en_CA')
    country = 'Canada'
    postal_code = Faker('postalcode', locale='en_CA')
    phone_number = Faker('phone_number', locale='en_CA')
    extension = 'todo'
    user = SubFactory(UserFactory)
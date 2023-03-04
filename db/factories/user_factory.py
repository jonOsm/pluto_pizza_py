import datetime
from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory
import random
from db.setup import get_scoped_session 
from db.models import UserModel


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = UserModel
        sqlalchemy_session = get_scoped_session() 
        sqlalchemy_session_persistence = "commit"

    # username = factory.Sequence(lambda n: "john%s" % n)
    # email = factory.LazyAttribute(lambda o: "%s@example.org" % o.username)
    # date_joined = factory.LazyFunction(datetime.datetime.now)

    email = Faker('ascii_email')
    email = Faker('ascii_email')
    email_verified = Faker('boolean', 
                           chance_of_getting_true=75)
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    disabled = Faker('boolean', 
                     chance_of_getting_true=5)
    hashed_password = "$2b$12$RjCfW4z96wrp2isyFMiTweQL/H/QaaKY8FjrH9/1F/HOiH6y4s4Qy"

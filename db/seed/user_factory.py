import datetime
import factory
import random
from db.setup import get_scoped_session
from db.models import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = get_scoped_session()

    # username = factory.Sequence(lambda n: "john%s" % n)
    # email = factory.LazyAttribute(lambda o: "%s@example.org" % o.username)
    # date_joined = factory.LazyFunction(datetime.datetime.now)

    email = "test"
    first_name = "test"
    last_name = "test"
    hashed_password = "test"

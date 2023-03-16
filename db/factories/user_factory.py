from factory import Faker, RelatedFactoryList
from factory.alchemy import SQLAlchemyModelFactory
from db.setup import scoped_session_local
from db.models import UserModel
from .address_factory import AddressFactory


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = UserModel
        sqlalchemy_session = scoped_session_local
        sqlalchemy_session_persistence = "commit"

    # username = factory.Sequence(lambda n: "john%s" % n)
    # email = factory.LazyAttribute(lambda o: "%s@example.org" % o.username)
    # date_joined = factory.LazyFunction(datetime.datetime.now)

    email = Faker("ascii_email")
    email_verified = Faker("boolean", chance_of_getting_true=75)
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    disabled = Faker("boolean", chance_of_getting_true=5)
    addresses = RelatedFactoryList(AddressFactory, "user", 2)
    hashed_password = "$2b$12$yQGJX8bHSq1Hr/ZSJ.7S8uTgZmAGKCdFqyI4Pm2w1WeKD.nJDCqs6"

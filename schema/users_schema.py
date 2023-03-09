from pydantic import BaseModel
from schema.addresses_schema import Address

example_schema = {
    "email": "foo@example.com",
    "first_name": "foo",
    "last_name": "bar",
}


class BaseUser(BaseModel):
    email: str
    first_name: str | None = None
    last_name: str | None = None


class BaseUserWithDisabled(BaseUser):
    disabled: bool | None = None


class User(BaseUserWithDisabled):
    id: str
    addresses: list[Address] | None

    class Config:
        schema_extra = {"example": example_schema}
        orm_mode = True


class UserInDB(BaseUserWithDisabled):
    disabled: bool | None = None
    hashed_password: str
    email_verified: bool | None


class UserIn(BaseUser):
    password: str

    class Config:
        schema_extra = {"example": {**example_schema, "password": "secret"}}


class UserDetails(BaseUser):
    pass

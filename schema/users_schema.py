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
    disabled: bool | None = None


class User(BaseUser):
    id: str
    access_token: str | None
    token_type: str | None
    addresses: list[Address] | None
    class Config:
        schema_extra = {"example": example_schema}
        orm_mode = True


class UserInDB(BaseUser):
    hashed_password: str
    email_verified: bool | None


class UserIn(BaseUser):
    password: str

    class Config:
        schema_extra = {"example": {**example_schema, "password": "secret"}}
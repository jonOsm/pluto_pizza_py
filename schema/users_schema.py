from pydantic import BaseModel, Field
from schema.addresses_schema import Address

example_schema = {
    "email": "foo@example.com",
    "first_name": "foo",
    "last_name": "bar",
}


class BaseUser(BaseModel):
    email: str = Field(min_length=5)
    first_name: str | None = None
    last_name: str | None = None


class BaseUserWithDisabled(BaseUser):
    disabled: bool | None = None


class User(BaseUserWithDisabled):
    id: int
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


class UserDelete(BaseModel):
    id: str

    class Config:
        orm_mode = True


class UserDetails(BaseUser):
    pass

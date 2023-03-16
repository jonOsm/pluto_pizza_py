import re
from pydantic import BaseModel, EmailStr, Field, SecretStr, validator
from schema.addresses_schema import Address

example_schema = {
    "email": "foo@example.com",
    "first_name": "foo",
    "last_name": "bar",
}


class BaseUser(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=64)
    last_name: str = Field(min_length=1, max_length=64)


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
    password: SecretStr = Field(min_length=8, max_length=32)

    @validator("password")
    def password_constraints(cls, v):
        try:
            pattern = re.compile(
                r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{0,}$"
            )
        except re.error as e:
            raise e

        if not pattern.match(v.get_secret_value()):
            raise ValueError(
                "Password must have at least 1 uppercase, 1 lowercase, 1 digit and 1 symbol."
            )
        return v

    class Config:
        schema_extra = {"example": {**example_schema, "password": "secret"}}


class UserDelete(BaseModel):
    id: str

    class Config:
        orm_mode = True


class UserDetails(BaseUser):
    pass

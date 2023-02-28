from pydantic import BaseModel

example_schema = {
    "email": "foo@example.com",
    "first_name": "foo",
    "last_name": "bar",
}


class User(BaseModel):
    email: str
    first_name: str | None = None
    last_name: str | None = None
    disabled: bool | None = None

    class Config:
        schema_extra = {"example": example_schema}


class UserInDB(User):
    hashed_password: str
    email_verified: bool | None


class UserIn(User):
    password: str

    class Config:
        schema_extra = {"example": {**example_schema, "password": "secret"}}


class UserOut(User):
    pass

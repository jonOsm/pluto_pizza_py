from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class User(BaseModel):
    email: str
    first_name: str | None = None
    last_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
    email_verified: bool = False


class UserIn(User):
    password: str


class UserOut(User):
    pass

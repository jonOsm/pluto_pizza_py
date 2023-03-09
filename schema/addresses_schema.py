from pydantic import BaseModel


class BaseAddress(BaseModel):
    label: str | None
    street: str
    unit: str | None
    city: str
    province: str
    postal_code: str
    phone_number: str
    extension: str | None


class AddressIn(BaseAddress):
    pass


class AddressInDB(BaseAddress):
    user_id: int
    pass


class Address(BaseAddress):
    user_id: int
    id: int

    class Config:
        orm_mode = True


class AddressDelete:
    id: int

    class Config:
        orm_mode = True

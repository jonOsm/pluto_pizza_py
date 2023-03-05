from pydantic import BaseModel

class BaseAddress(BaseModel):
    user_id: int
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
     
class Address(BaseAddress):
    id: int
    class Config:
        orm_mode = True
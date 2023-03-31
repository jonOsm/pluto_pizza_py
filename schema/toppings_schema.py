from pydantic import BaseModel


class BaseToppingType(BaseModel):
    name: str


class ToppingType(BaseToppingType):
    id: int

    class Config:
        orm_mode = True


class BaseTopping(BaseModel):
    name: str
    base_price: float
    topping_type: ToppingType


class ToppingIn(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Topping(BaseTopping):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from .toppings_schema import Topping


class CrustType(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CrustThickness(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CheeseType(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CheeseAmt(BaseModel):
    id: int
    name: str
    base_price: float

    class Config:
        orm_mode = True


class SauceType(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SauceAmt(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductCustomizationDefault(BaseModel):
    id: int
    is_default: bool
    toppings: list[Topping]
    crust_type: CrustType
    crust_thickness: CrustThickness
    cheese_type: CheeseType
    cheese_amt: CheeseAmt
    sauce_type: SauceType
    sauce_amt: SauceAmt

    class Config:
        orm_mode = True

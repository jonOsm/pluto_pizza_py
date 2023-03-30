from pydantic import BaseModel
from .toppings_schema import Topping


class BaseProductCustomizationField(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CrustType(BaseProductCustomizationField):
    pass


class CrustThickness(BaseProductCustomizationField):
    pass


class CheeseType(BaseProductCustomizationField):
    pass


class CheeseAmt(BaseProductCustomizationField):
    base_price: float


class SauceType(BaseProductCustomizationField):
    pass


class SauceAmt(BaseProductCustomizationField):
    pass


class ProductSize(BaseProductCustomizationField):
    pass


class ProductCustomizationEssential(BaseModel):
    product_size: ProductSize


class ProductCustomizationDefault(BaseModel):
    id: int
    is_default: bool
    toppings: list[Topping]
    product_size: ProductSize
    crust_type: CrustType
    crust_thickness: CrustThickness
    cheese_type: CheeseType
    cheese_amt: CheeseAmt
    sauce_type: SauceType
    sauce_amt: SauceAmt

    class Config:
        orm_mode = True


class ProductCustomizationOptions(BaseModel):
    # would normally pluralize names but not doing so
    # simplifies FE logic
    toppings: list[Topping]
    product_size: list[ProductSize]
    crust_type: list[CrustType]
    crust_thickness: list[CrustThickness]
    cheese_amt: list[CheeseAmt]
    cheese_type: list[CheeseType]
    sauce_amt: list[SauceAmt]
    sauce_type: list[SauceType]

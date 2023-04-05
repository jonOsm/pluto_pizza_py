from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from schema.products_schema import Product, ProductEssentials
from util.proxy import ProxyHackGetter
from .toppings_schema import Topping, ToppingIn


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


class ProductCustomizationBase(BaseModel):
    product_size: ProductSize
    crust_type: CrustType
    crust_thickness: CrustThickness
    cheese_type: CheeseType
    cheese_amt: CheeseAmt
    sauce_type: SauceType
    sauce_amt: SauceAmt

    class Config:
        orm_mode = True


class ProductCustomizationDefault(ProductCustomizationBase):
    id: int
    toppings: list[Topping]
    is_default: bool

    class Config:
        orm_mode = True
        getter_dict = ProxyHackGetter


class ProductCustomizationOut(ProductCustomizationBase):
    id: int
    product: ProductEssentials
    toppings: list[Topping]
    is_default: bool

    class Config:
        orm_mode = True
        getter_dict = ProxyHackGetter


class ProductCustomizationIn(BaseModel):
    toppings: list[ToppingIn]
    product_id: int
    product_size_id: int
    crust_type_id: int
    crust_thickness_id: int
    cheese_type_id: int
    cheese_amt_id: int
    sauce_type_id: int
    sauce_amt_id: int

    class Config:
        orm_mode = True


class ProductCustomizationOptions(BaseModel):
    # would normally pluralize names but not doing so
    # simplifies FE logic
    toppings: list[Topping]
    additional_toppings: list[Topping]
    product_size: list[ProductSize]
    crust_type: list[CrustType]
    crust_thickness: list[CrustThickness]
    cheese_amt: list[CheeseAmt]
    cheese_type: list[CheeseType]
    sauce_amt: list[SauceAmt]
    sauce_type: list[SauceType]

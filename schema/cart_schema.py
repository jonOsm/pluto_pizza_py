from pydantic import BaseModel
from db.models import CartItemModel
from schema.product_customization_schema import (
    ProductCustomizationDefault,
    ProductCustomizationIn,
    ProductCustomizationOut,
)


class CartItem(BaseModel):
    # TODO: create ProductCustomization schema specific to carts
    product_customization: ProductCustomizationDefault

    class Config:
        orm_mode = True


class CartItemIn(CartItem):
    product_customization: ProductCustomizationIn

    class Config:
        orm_mode = True

    pass


class CartItemOut(BaseModel):
    id: int
    cart_id: int
    product_customization: ProductCustomizationOut

    class Config:
        orm_mode = True


class Cart(BaseModel):
    id: int
    user_id: int | None
    is_active: bool
    cart_items: list[CartItem]

    class Config:
        orm_mode = True

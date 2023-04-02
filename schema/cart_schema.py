from pydantic import BaseModel
from db.models import CartItemModel
from schema.product_customization_schema import ProductCustomizationIn


class CartItem(BaseModel):
    # TODO: create ProductCustomization schema specific to carts
    product_customization: ProductCustomizationIn

    class Config:
        orm_mode = True


class CartItemIn(CartItem):
    pass


class CartItemOut(BaseModel):
    id: int
    cart_id: int

    class Config:
        orm_mode = True


class Cart(BaseModel):
    id: int
    user_id: int | None
    is_active: bool
    cart_items: list[CartItem]

    class Config:
        orm_mode = True

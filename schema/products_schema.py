from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    base_price: float
    is_draft: bool
    stock: int
    sku: str
    image_url: str

    class Config:
        orm_mode = True


class ProductWithEssentialCustomization(Product):
    product_size: "ProductSize"

    class Config:
        orm_mode = True


class ProductEssentials(BaseModel):
    name: str
    id: int
    base_price: float
    image_url: str

    class Config:
        orm_mode = True


# down here to handle circular imports
# TODO: look into better way to handle circular imports
from schema.product_customization_schema import (
    ProductSize,
)

ProductWithEssentialCustomization.update_forward_refs()

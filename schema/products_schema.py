from pydantic import BaseModel

from schema.product_customization_schema import (
    ProductCustomizationDefault,
    ProductCustomizationEssential,
    ProductSize,
)


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
    product_size: ProductSize

    class Config:
        orm_mode = True

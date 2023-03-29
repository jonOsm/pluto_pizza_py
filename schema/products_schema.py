from pydantic import BaseModel

from schema.product_customization_schema import ProductSize


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
    product_size_name: str

    class Config:
        orm_mode = True

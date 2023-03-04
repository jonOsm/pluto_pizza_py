from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str 
    base_price: float
    base_size: str
    is_draft: bool
    stock: int
    sku: str
    image_url: str

    class Config:
        orm_mode = True
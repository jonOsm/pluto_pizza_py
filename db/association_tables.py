from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.models import ToppingModel
from db.setup import Base


product_customization_toppings_table = Table(
    "product_customization_toppings",
    Base.metadata,
    Column(
        "product_customization_id",
        ForeignKey("product_customizations.id", ondelete="cascade"),
        primary_key=True,
    ),
    Column("topping_id", ForeignKey("toppings.id"), primary_key=True),
)


class ProductCustomizationToppings(Base):
    "product_customization_toppings",
    topping_id: Mapped[int] = mapped_column(ForeignKey("toppings.id"), primary_key=True)
    product_customization_id: Mapped[int] = mapped_column(
        ForeignKey("product_customizations.id"), primary_key=True
    )

    topping: Mapped[ToppingModel] = relationship(backref="product")

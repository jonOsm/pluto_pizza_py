from sqlalchemy import Column, ForeignKey, Table

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

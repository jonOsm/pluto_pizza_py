from db.setup import Base
from sqlalchemy import Boolean, ForeignKey, String, Table, sql
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .association_tables import product_customization_toppings_table

# Necessary for sqlite to handle altering constraints:
# https://stackoverflow.com/a/62651160
# convention = {
#     "ix": "ix_%(column_0_label)s",
#     "uq": "uq_%(table_name)s_%(column_0_name)s",
#     "ck": "ck_%(table_name)s_%(constraint_name)s",
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#     "pk": "pk_%(table_name)s",
# }


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    email_verified: Mapped[bool] = mapped_column(server_default=sql.false())
    first_name: Mapped[str]
    last_name: Mapped[str]
    disabled: Mapped[bool] = mapped_column(server_default=sql.false())
    hashed_password: Mapped[str]

    addresses: Mapped[list["AddressModel"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    # orders: Mapped[list["Order"]] = relationship(back_populates="user")


class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    base_price: Mapped[float]
    # base_size: Mapped[str]
    is_draft: Mapped[bool] = mapped_column(default=True)
    stock: Mapped[int] = mapped_column(default=0)
    sku: Mapped[str] = mapped_column(String(50))
    image_url: Mapped[str]

    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="product"
    )


class AddressModel(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )
    label: Mapped[str | None] = mapped_column(String(50))
    street: Mapped[str]
    unit: Mapped[str | None]
    city: Mapped[str]
    province: Mapped[str]
    country: Mapped[str] = mapped_column(default="Canada")
    postal_code: Mapped[str]
    phone_number: Mapped[str]
    extension: Mapped[str | None]

    user: Mapped[UserModel] = relationship(back_populates="addresses")


class ToppingModel(Base):
    __tablename__ = "toppings"
    id: Mapped[int] = mapped_column(primary_key=True)
    type_id: Mapped[int] = mapped_column(ForeignKey("topping_types.id"))
    name: Mapped[str]
    base_price: Mapped[float] = mapped_column()
    # debating whether this should be computed based on price
    # is_premium: Mapped[bool]
    topping_type: Mapped["ToppingTypeModel"] = relationship(back_populates="toppings")
    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        secondary=product_customization_toppings_table, back_populates="toppings"
    )


class ToppingTypeModel(Base):
    __tablename__ = "topping_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    toppings: Mapped[ToppingModel] = relationship(back_populates="topping_type")


class CrustTypeModel(Base):
    __tablename__ = "crust_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="crust_type"
    )


class CrustThicknessModel(Base):
    __tablename__ = "crust_thicknesses"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="crust_thickness"
    )


class CheeseTypeModel(Base):
    __tablename__ = "cheese_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="cheese_type"
    )


class CheeseAmtModel(Base):
    __tablename__ = "cheese_amts"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    base_price: Mapped[float]
    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="cheese_amt"
    )


class SauceTypeModel(Base):
    __tablename__ = "sauce_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="sauce_type"
    )


class SauceAmtModel(Base):
    __tablename__ = "sauce_amts"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="sauce_amt"
    )


class ProductSizeModel(Base):
    __tablename__ = "product_sizes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    base_price: Mapped[float]

    product_customizations: Mapped[list["ProductCustomizationsModel"]] = relationship(
        back_populates="product_size"
    )


class ProductCustomizationsModel(Base):
    __tablename__ = "product_customizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_default: Mapped[bool] = mapped_column(default=False)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE")
    )

    crust_type_id: Mapped[int] = mapped_column(ForeignKey("crust_types.id"))
    crust_thickness_id: Mapped[int] = mapped_column(ForeignKey("crust_thicknesses.id"))
    cheese_type_id: Mapped[int] = mapped_column(ForeignKey("cheese_types.id"))
    cheese_amt_id: Mapped[int] = mapped_column(ForeignKey("cheese_amts.id"))
    sauce_type_id: Mapped[int] = mapped_column(ForeignKey("sauce_types.id"))
    sauce_amt_id: Mapped[int] = mapped_column(ForeignKey("sauce_amts.id"))
    product_size_id: Mapped[int] = mapped_column(ForeignKey("product_sizes.id"))

    product: Mapped[ProductModel] = relationship(
        back_populates="product_customizations",
    )
    toppings: Mapped[ToppingModel] = relationship(
        secondary=product_customization_toppings_table,
        back_populates="product_customizations",
    )
    crust_type: Mapped[CrustTypeModel] = relationship(
        back_populates="product_customizations"
    )
    crust_thickness: Mapped[CrustThicknessModel] = relationship(
        back_populates="product_customizations"
    )
    cheese_type: Mapped[CheeseTypeModel] = relationship(
        back_populates="product_customizations"
    )
    cheese_amt: Mapped[CheeseAmtModel] = relationship(
        back_populates="product_customizations"
    )
    sauce_type: Mapped[SauceTypeModel] = relationship(
        back_populates="product_customizations"
    )
    sauce_amt: Mapped[SauceAmtModel] = relationship(
        back_populates="product_customizations"
    )
    product_size: Mapped[ProductSizeModel] = relationship(
        back_populates="product_customizations"
    )

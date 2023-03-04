from db.setup import Base
from sqlalchemy import ForeignKey, String, DateTime, func, sql
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Necessary for sqlite to handle altering constraints: https://stackoverflow.com/a/62651160
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

    addresses: Mapped[list["AddressModel"]] = relationship(back_populates="user")
    # orders: Mapped[list["Order"]] = relationship(back_populates="user")

class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    base_price: Mapped[float]
    base_size: Mapped[str]
    is_draft: Mapped[bool] = mapped_column(default=True)
    stock: Mapped[int] = mapped_column(default=0)
    sku: Mapped[str] = mapped_column(String(50))
    image_url: Mapped[str]

class AddressModel(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    label: Mapped[str] = mapped_column(String(50))
    street: Mapped[str]
    unit: Mapped[str | None]
    city: Mapped[str]
    province: Mapped[str]
    country: Mapped[str] = mapped_column(default='Canada')
    postal_code: Mapped[str]
    phone_number: Mapped[str]
    extension: Mapped[str]

    user: Mapped[UserModel] = relationship(back_populates="addresses")
#     orders: Mapped[List["Order"]] = relationship(back_populates="address")


# class Order(db.Model):
#     __tablename__ = "order"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
#     address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))
#     # tax_id
#     order_status_id: Mapped[int] = mapped_column(ForeignKey("order_status.id"))

#     user: Mapped[User] = relationship(back_populates="orders")
#     address: Mapped[Address] = relationship(back_populates="orders")
#     order_status: Mapped["OrderStatus"] = relationship(back_populates="orders")


# class OrderStatus(db.Model):
#     __tablename__ = "order_status"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(unique=True)

#     orders: Mapped[List["Order"]] = relationship(back_populates="order_status")

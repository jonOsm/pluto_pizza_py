from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from db.models import CartItemModel, CartModel


def read_user_cart(db: Session, user_id):
    stmt = (
        select(CartModel)
        .where((CartModel.user_id == user_id))
        .where(CartModel.is_active)
    )
    return db.scalars(stmt).first()


def create_cart_item(db: Session, cart_item: CartItemModel):
    db.add(cart_item)
    db.commit()
    return cart_item

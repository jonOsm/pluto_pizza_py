from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from db.models import (
    CartItemModel,
    CartModel,
)


def read_active_user_cart(db: Session, user_id):
    stmt = (
        select(CartModel)
        .where((CartModel.user_id == user_id))
        .where(CartModel.is_active)
        .order_by(desc(CartModel.created_at))
    )
    return db.scalars(stmt).first()


def create_cart_item(db: Session, cart_item: CartItemModel):
    db.add(cart_item)
    db.commit()
    return cart_item


def create_cart(db: Session, cart: CartModel):
    db.add(cart)
    db.commit()
    return cart


def delete_cart_item(db: Session, cart_item_id: int):
    cart_item = db.get(CartItemModel, cart_item_id)
    db.delete(cart_item)
    db.commit()
    return None if cart_item is None else cart_item.id

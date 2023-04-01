from fastapi import APIRouter, Depends
from api.auth import get_current_active_user
from sqlalchemy.orm import Session
from api.crud.cart_crud import create_cart_item, read_user_cart
from db.models import CartItemModel, ProductCustomizationsModel, ToppingModel
from db.setup import get_db
from schema.cart_schema import Cart, CartItem, CartItemIn
from schema.toppings_schema import ToppingIn
from schema.users_schema import User

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("/")
def show_active_user_cart(
    user: User = Depends(get_current_active_user), db: Session = Depends(get_db)
) -> Cart | None:
    return read_user_cart(db, user.id)


# how to handle anon users?
@router.post("/item")
def store_cart_item(
    cart_item: CartItemIn,
    user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> CartItem:
    # fetch cart
    # if no active cart, create cart
    # store cart_item
    cart_item_dict = cart_item.dict()
    new_toppings = [
        {"topping_id": raw_topping["id"]}
        for raw_topping in cart_item_dict["product_customization"]["toppings"]
    ]
    del cart_item_dict["product_customization"]["toppings"]
    new_product_cust = ProductCustomizationsModel(
        **cart_item_dict["product_customization"]
    )
    new_product_cust.toppings.append(new_toppings[0])
    # new_product_cust.toppings = new_toppings
    cart_item_db = CartItemModel(product_customization=new_product_cust, cart_id=1)
    return create_cart_item(db, cart_item_db)
    # return cart item

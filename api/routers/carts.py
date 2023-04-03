from fastapi import APIRouter, Depends
from api.auth import get_current_active_user
from sqlalchemy.orm import Session
from api.crud.cart_crud import (
    create_cart,
    create_cart_item,
    read_active_user_cart,
)
from db.models import (
    CartItemModel,
    CartModel,
    ProductCustomizationsModel,
    ProductCustomizationToppingsModel,
)
from db.setup import get_db
from schema.cart_schema import Cart, CartItemIn, CartItemOut
from schema.users_schema import User

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("/")
def show_active_user_cart(
    user: User = Depends(get_current_active_user), db: Session = Depends(get_db)
) -> Cart | None:
    return read_active_user_cart(db, user.id)


# TODO: Consideration - how will we handle anon users?
# TODO: this is messy, may wish to use multiple requests on the FE instead
@router.post("/item")
def store_cart_item(
    cart_item: CartItemIn,
    user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> CartItemOut:
    cart = read_active_user_cart(db, user.id)
    if not cart:
        cart = CartModel(user_id=user.id, is_active=True)
        cart = create_cart(db, cart)

    cart_item_dict = cart_item.dict()
    new_toppings_association = [
        ProductCustomizationToppingsModel(topping_id=raw_topping["id"])
        for raw_topping in cart_item_dict["product_customization"]["toppings"]
    ]
    del cart_item_dict["product_customization"]["toppings"]
    new_product_cust = ProductCustomizationsModel(
        **cart_item_dict["product_customization"]
    )
    new_product_cust.toppings_association = new_toppings_association
    cart_item_db = CartItemModel(
        product_customization=new_product_cust, cart_id=cart.id
    )
    return create_cart_item(db, cart_item_db)

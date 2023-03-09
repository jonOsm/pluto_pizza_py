from sqlalchemy.orm import Session 
from fastapi import APIRouter, Body, Depends
from api.crud.addresses_crud import create_address
from schema.addresses_schema import AddressIn, Address
from api.auth import get_current_active_user
from schema.users_schema import User
from db.setup import get_db

router = APIRouter(prefix="/addresses", tags=['addresses'])

@router.get("/")
def get_all_user_addresses(user_id:str):
    pass

@router.post("/create")
def store_new_address(address: AddressIn = Body(), current_user: User = Depends(get_current_active_user), db:Session=Depends(get_db)) -> Address:
    address.user_id = current_user.id
    return create_address(db, address)
    

    
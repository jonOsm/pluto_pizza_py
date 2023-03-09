from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException, status 
from api.crud.addresses_crud import create_address, address_belongs_to_user, delete_address 
from schema.addresses_schema import (
    AddressDelete,
    AddressIn,
    Address,
    AddressInDB,
)
from api.auth import get_current_active_user
from schema.users_schema import User
from db.setup import get_db

router = APIRouter(prefix="/addresses", tags=["addresses"])


@router.get("/")
def get_all_user_addresses(user_id: str):
    pass


@router.post("/create")
def store_address(
    address: AddressIn = Body(),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> Address:
    address_to_create = AddressInDB(**address.dict(), user_id=current_user.id)
    return create_address(db, address_to_create)


@router.delete("/{address_id}")
def destroy_address(
    address_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> AddressDelete:
    # check that address belongs to user - crud method?
    if(not address_belongs_to_user(db, current_user, address_id)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User may not delete this addesses"
        )
        
    # delete the address - crud method.
    return AddressDelete(id=delete_address(db, address_id))

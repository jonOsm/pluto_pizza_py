from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException, status
from api.crud.addresses_crud import (
    create_address,
    address_belongs_to_user,
    delete_address,
    update_address,
)
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

user_unauthorized_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User unauthorized. Access to resource rejected.",
)

resource_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Unable to find the specified resource.",
)


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
    if not address_belongs_to_user(db, current_user, address_id):
        raise user_unauthorized_exception

    address_deleted_id = delete_address(db, address_id)
    if address_deleted_id is None:
        raise resource_not_found_exception

    return AddressDelete(id=address_deleted_id)


@router.put("/{address_id}")
def modify_address(
    address_id: int,
    address: AddressIn,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> Address:
    # check that address belongs to user
    if not address_belongs_to_user(db, current_user, address_id):
        raise user_unauthorized_exception

    address_to_edit = AddressInDB(**address.dict(), user_id=current_user.id)
    # modify address and return modified address
    return update_address(db, address_to_edit, address_id)

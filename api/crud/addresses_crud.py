from sqlalchemy import select
from sqlalchemy.orm import Session
from schema.addresses_schema import AddressDelete, AddressInDB, Address
from db.models import AddressModel
from schema.users_schema import User


def create_address(db: Session, address_to_create: AddressInDB) -> Address:
    address = AddressModel(**address_to_create.dict())
    db.add(address)
    db.commit()

    return address

def address_belongs_to_user(db: Session, user: User, address_id: int) -> bool:
    address = db.get(AddressModel, address_id)
    return address.user_id == user.id

def delete_address(db:Session, address_id) -> AddressDelete:
    address = db.get(AddressModel, address_id)
    db.delete(address)
    db.commit()
    return address.id
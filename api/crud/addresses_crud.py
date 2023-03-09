from sqlalchemy import select
from sqlalchemy.orm import Session
from schema.addresses_schema import AddressInDB, Address
from db.models import AddressModel


def create_address(db: Session, address_to_create: AddressInDB) -> Address:
    address = AddressModel(**address_to_create.dict())
    db.add(address)
    db.commit()

    return address

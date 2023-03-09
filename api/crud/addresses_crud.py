from sqlalchemy import select
from sqlalchemy.orm import Session 
from schema.addresses_schema import AddressIn, Address
from db.models import AddressModel

def create_address(db:Session, address_in: AddressIn) -> Address:
    address = AddressModel(AddressModel(**address_in.dict()))
    db.add(address)
    db.commit()

    return Address(address)


    

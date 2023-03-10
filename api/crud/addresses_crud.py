from sqlalchemy import select, update
from sqlalchemy.orm import Session
from schema.addresses_schema import AddressDelete, AddressInDB, Address
from db.models import AddressModel
from schema.users_schema import User


def read_address(db: Session, address_id: int):
    return db.get(AddressModel, address_id)


def create_address(db: Session, address_to_create: AddressInDB) -> Address:
    address = AddressModel(**address_to_create.dict())
    db.add(address)
    db.commit()

    return address


def address_belongs_to_user(db: Session, user: User, address_id: int) -> bool:
    address = db.get(AddressModel, address_id)
    return address.user_id == user.id


def delete_address(db: Session, address_id) -> AddressDelete:
    address = db.get(AddressModel, address_id)
    db.delete(address)
    db.commit()
    return address.id


def update_address(
    db: Session, address_to_edit: AddressInDB, address_id: int
) -> Address:
    stmt = (
        update(AddressModel)
        .where(AddressModel.id == address_id)
        .values(**address_to_edit.dict())
    )
    db.execute(stmt)
    db.commit()

    return read_address(db, address_id)

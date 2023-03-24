from typing import Sequence
from db.models import ToppingModel
from sqlalchemy import select
from sqlalchemy.orm import Session


def read_toppings(db: Session) -> Sequence[ToppingModel]:
    stmt = select(ToppingModel)
    return db.scalars(stmt).all()

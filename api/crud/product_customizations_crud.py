from sqlalchemy import select
from sqlalchemy.orm import Session


def read_all_secondary_customization(db: Session, model: any):
    stmt = select(model)

    return db.scalars(stmt).all()

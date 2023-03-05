from datetime import datetime
from sqlalchemy import create_engine, func 
from sqlalchemy.orm import sessionmaker, DeclarativeBase, scoped_session, Mapped, mapped_column
import configparser

config = configparser.ConfigParser()
config.read("./alembic.ini")

engine = create_engine(
    config["alembic"]["sqlalchemy.url"],
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
scoped_session_local = scoped_session(SessionLocal)

class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(),
                                                  server_onupdate=func.now())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
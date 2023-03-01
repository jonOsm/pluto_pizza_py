from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, scoped_session
import configparser

config = configparser.ConfigParser()
config.read("./alembic.ini")

engine = create_engine(
    config["alembic"]["sqlalchemy.url"],
    connect_args={
        "check_same_thread": False,
    },
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_scoped_session():
    return scoped_session(SessionLocal)

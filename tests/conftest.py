from fastapi.testclient import TestClient
import pytest
from ..main import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.setup import Base
from db.setup import get_db


@pytest.fixture
def client():
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    client = TestClient(app)
    app.dependency_overrides[get_db] = override_get_db

    yield client
    Base.metadata.drop_all(bind=engine)

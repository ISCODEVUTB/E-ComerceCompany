# test/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.logic.database import Base  # Importa tus modelos

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://talento:cartagena@nodossolutions.com:1435/ecommerce?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

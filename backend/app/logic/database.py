from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from decouple import config

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://talento:cartagena@nodossolutions.com:1435/ecommerce?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

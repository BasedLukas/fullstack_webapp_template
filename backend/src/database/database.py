from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import get_settings
import logging

log = logging.getLogger(__name__)
settings = get_settings()
username = settings.username_db
password = settings.password
host = settings.host
port = settings.port  # Default PostgreSQL port
database = settings.database  # The database name

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
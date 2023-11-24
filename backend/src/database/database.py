from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these credentials with your actual PostgreSQL credentials
username = "test"
password = "test"  # The password you set when running the Docker container
host = "localhost"
port = "5432"  # Default PostgreSQL port
database = "vue-app-db"  # The database name

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

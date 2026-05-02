from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set")

# Render даёт postgres://, SQLAlchemy 2.0 требует postgresql://
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(database_url)

sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import  create_engine 
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(database_url)

sessionlocal = sessionmaker(bind=engine , autocommit=False , autoflush=False)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()



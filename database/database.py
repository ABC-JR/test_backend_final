from sqlalchemy import  create_engine 
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load_dotenv()
local_url =  "postgresql://pmdb_8ikr_user:eeFMRQrYTWzfUhJctZRW5CbfbJz1vVit@dpg-d7o30hpf9bms738rsgn0-a.oregon-postgres.render.com/pmdb_8ikr"




engine = create_engine(local_url)

sessionlocal = sessionmaker(bind=engine , autocommit=False , autoflush=False)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()



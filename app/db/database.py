from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL) #core engine

'''
so this is my first time working with fastapi + orm , thus i am documenting it so i can recall this.
IGNORE
well the flow is each api will create a session for itself , and session will have core part as an engine
the engine will send request to psycopg2 driver and then driver will send it to postgres .
'''
SessionLocal = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush=False
) #main session for apis , we turned autocommit and flush to false as it will create a secure flow for apis
# no api can call the DTQ (database transaction query) on  their own

Base = declarative_base() # ill inherit this for models

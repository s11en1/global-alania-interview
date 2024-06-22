from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = 'postgresql://postgres:adminpass@localhost:5432/global_alania'

engine = create_engine(DB_URI)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
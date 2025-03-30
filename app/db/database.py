from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./db/database.db"
engine = create_engine(DATABASE_URL) # Optionally, include 'echo=True' for logging

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

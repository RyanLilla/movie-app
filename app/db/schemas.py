from sqlmodel import SQLModel
from typing import Optional

class MovieRead(SQLModel):
    id: int
    title: str
    overview: Optional[str] = None
    release_date: Optional[str] = None

class MovieCreate(SQLModel):
    # TODO
    ...

class MovieUpdate(SQLModel):
    # TODO
    ...
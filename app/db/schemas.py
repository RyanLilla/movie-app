from sqlmodel import SQLModel
from typing import Optional

from app.db.models import MovieBase

class MovieResponse(MovieBase):
    id: int

class MovieCreate(SQLModel):
    # TODO
    ...

class MovieUpdate(SQLModel):
    # TODO
    ...
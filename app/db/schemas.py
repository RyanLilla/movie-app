from sqlmodel import SQLModel
from typing import Optional

from app.db.models import MovieBase

class MovieResponse(MovieBase):
    id: int
    poster_url: Optional[str] = None
    backdrop_url: Optional[str] = None

class MovieCreate(SQLModel):
    # TODO
    ...

class MovieUpdate(SQLModel):
    # TODO
    ...
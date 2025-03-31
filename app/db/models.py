from sqlmodel import SQLModel, Field
from typing import Optional


class MovieBase(SQLModel):
    overview: Optional[str] = None
    release_date: Optional[str] = None
    title: Optional[str] = None

class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    genre_ids: Optional[str] = None 
    vote_average: Optional[int] = None
    vote_count: Optional[int] = None
    popularity: Optional[int] = None
from fastapi.datastructures import Default
from sqlalchemy import true
from sqlmodel import SQLModel, Field
from typing import Optional

class Movie(SQLModel, table=True):
    id: Optional[int] = Field(Default=None, primary_key=True)
    genre_ids: Optional[str] = None  # Stored as TEXT, possibly comma-separated or JSON string
    overview: Optional[str] = None
    popularity: Optional[int] = None
    release_date: Optional[str] = None
    title: Optional[str] = None
    vote_average: Optional[int] = None
    vote_count: Optional[int] = None
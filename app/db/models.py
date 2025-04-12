from sqlmodel import SQLModel, Field
from typing import Optional

from app.db.schemas import MovieBase


class Movie(MovieBase, table=True):
    __tablename__ = "movie"
    id: Optional[int] = Field(default=None, primary_key=True)
    genre_ids: Optional[str] = None 
    vote_average: Optional[int] = None
    vote_count: Optional[int] = None
    popularity: Optional[int] = None
    poster_url: Optional[str] = None
    backdrop_url: Optional[str] = None

class ProductionCompany(SQLModel, table=True):
    __tablename__ = "production_company"
    id: int = Field(primary_key=True)
    name: str
    logo_path: Optional[str] = None
    origin_country: Optional[str] = None

class MovieProductionCompanyLink(SQLModel, table=True):
    __tablename__ = "movie_production_company_link"
    movie_id: int = Field(foreign_key="movie.id", primary_key=True)
    company_id: int = Field(foreign_key="production_company.id", primary_key=True)
from sqlmodel import SQLModel
from typing import Optional, List


class MovieBase(SQLModel):
    overview: Optional[str] = None
    release_date: Optional[str] = None
    title: Optional[str] = None

class GenreBase(SQLModel):
    name: str

class GenreResponse(GenreBase):
    id: int

class MovieResponse(MovieBase):
    id: int
    poster_url: Optional[str] = None
    backdrop_url: Optional[str] = None
    popularity: Optional[float] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    genres: List[GenreResponse] = []

class MovieCreate(SQLModel):
    # TODO
    ...

class MovieUpdate(SQLModel):
    # TODO
    ...

class ProductionCompanyBase(SQLModel):
    name: str
    logo_path: Optional[str] = None
    origin_country: Optional[str] = None

class ProductionCompanyCreate(ProductionCompanyBase):
    id: int

class ProductionCompanyResponse(ProductionCompanyBase):
    id: int

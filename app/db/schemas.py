from sqlmodel import SQLModel
from typing import Optional


class MovieBase(SQLModel):
    overview: Optional[str] = None
    release_date: Optional[str] = None
    title: Optional[str] = None

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

class ProductionCompanyBase(SQLModel):
    name: str
    logo_path: Optional[str] = None
    origin_country: Optional[str] = None

class ProductionCompanyCreate(ProductionCompanyBase):
    id: int

class ProductionCompanyResponse(ProductionCompanyBase):
    id: int

# Join table schema (if needed)
class MovieProductionCompanyLink(SQLModel):
    movie_id: int
    company_id: int
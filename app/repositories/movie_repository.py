from app.db.database import get_session
from app.db.models import Movie
from sqlmodel import select

def get_movie_by_id(movie_id: int):
    # TODO
    ...
from app.db.database import get_session
from app.db.models import Movie
from sqlmodel import select

def get_movie_by_id(movie_id: int):
    with get_session() as session:
        return session.exec(select(Movie).where(Movie.id == movie_id)).first()

def insert_movie(movie: Movie):
    with get_session() as session:
        session.add(movie)
        session.commit()
        session.refresh(movie)
        return movie
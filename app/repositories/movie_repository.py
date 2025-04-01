from app.db.database import get_session
from app.db.models import Movie
from sqlmodel import select

def get_movie_by_id(movie_id: int):
    """
    Retrieve a movie by its ID from the database.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        Movie: The movie object if found, otherwise None.
    """
    with get_session() as session:
        return session.exec(select(Movie).where(Movie.id == movie_id)).first()

def get_all_movies():
    """
    Retrieve all movies from the database.

    Returns:
        list[Movie]: A list of all Movie objects in the database.
    """
    with get_session() as session:
        return session.exec(select(Movie)).all()

def insert_movie(movie: Movie):
    """
    Insert a new movie into the database.

    Args:
        movie (Movie): The Movie object to insert.

    Returns:
        Movie: The inserted Movie object with updated fields (e.g., ID).
    """
    with get_session() as session:
        session.add(movie)
        session.commit()
        session.refresh(movie)
        return movie
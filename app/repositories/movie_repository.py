from sqlmodel import select
from app.db.database import get_session
from app.db.models import Movie, Genre, MovieGenreLink


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


def get_movie_by_title(title: str):
    """
    Retrieve a movie by its title from the database.

    Args:
        title (str): The title of the movie to retrieve.

    Returns:
        Movie: The movie object if found, otherwise None.
    """
    with get_session() as session:
        return session.exec(select(Movie).where(Movie.title == title)).first()


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


def get_genres_for_movie(movie_id: int):
    """
    Retrieve all genres associated with a given movie ID.

    Args:
        movie_id (int): The ID of the movie.

    Returns:
        list[Genre]: A list of Genre objects linked to the movie.
    """
    with get_session() as session:
        statement = (
            select(Genre)
            .join(MovieGenreLink, Genre.id == MovieGenreLink.genre_id)
            .where(MovieGenreLink.movie_id == movie_id)
        )
        return session.exec(statement).all()
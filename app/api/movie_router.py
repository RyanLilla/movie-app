from fastapi import APIRouter, HTTPException
import app.services.movie_service as movie_service
from app.db.schemas import MovieResponse


router = APIRouter()

@router.get("/movie")
async def welcome():
    return {"message": "Movie App : Movie Route"}

@router.get("/movie/{movie_id}", response_model=MovieResponse)
async def get_watched_movie_by_id(movie_id: int):
    """
    Retrieve a movie by its ID.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        MovieResponse: The movie details if found.

    Raises:
        HTTPException: If no movie is found for the specified ID.
    """
    movie = movie_service.get_watched_movie_by_id(movie_id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="No movie found for the specified ID.")
    
    return movie

@router.get("/search/movie", response_model=list[MovieResponse])
async def search_movie_by_title(query: str):
    """
    Search for movies by their original, translated, and alternative titles.

    Args:
        query (str): The title of the movie to search for.

    Returns:
        MovieResponse: The movie details if found.

    Raises:
        HTTPException: If no movie is found for the specified query.
    """
    if not query:
        query = "The Gorge"
    
    movie_list = movie_service.search_movie_by_title(query=query)
    if movie_list is None:
        raise HTTPException(status_code=404, detail="No movies found for the specified query.")
    
    return movie_list

@router.get("/movies/all", response_model=list[MovieResponse])
async def get_all_watched_movies():
    """
    Retrieve all movies from the local database.

    Returns:
        list[MovieResponse]: A list of all movies in the database.

    Raises:
        HTTPException: If no movies are found in the database.
    """
    movies = movie_service.get_all_watched_movies_from_db()
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found.")
    
    return movies
    
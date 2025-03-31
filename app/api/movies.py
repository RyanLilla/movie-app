from fastapi import APIRouter, HTTPException

from app.db.schemas import MovieResponse
from app.services.movie_service import get_or_fetch_movie


router = APIRouter()

@router.get("/movie")
async def get_movie_by_id():
    return {"message": "Hello, Movie App : Movie Controller"}

@router.get("/movie/{movie_id}", response_model=MovieResponse)
async def get_movie_by_id(movie_id: int):
    movie = get_or_fetch_movie(movie_id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="No movie found for the specified ID.")
    
    return movie
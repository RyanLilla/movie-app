from fastapi import APIRouter


router = APIRouter()

@router.get("/movie/", tags=["movie"])
async def get_movie_by_id():
    ...
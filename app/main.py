from contextlib import asynccontextmanager
from pprint import pprint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import movie_router
from .db.database import create_db_and_tables
from .utils.movie_utils import MovieUtils
# from .services.movie_service import get_or_fetch_movie


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform startup tasks like creating the database tables
    create_db_and_tables()
    
    # Yield control back to FastAPI to start processing requests
    yield
    
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_router.router)

@app.get("/")
async def root():
    update_movie = False
    if update_movie:
        # MovieUtils.update_movie_urls()
        # print("Movie URLs updated successfully!")
        
        movie_ids = []
        # MovieUtils.bulk_add_movies_by_movie_ids(movie_ids)

    return {"message": "Hello, Movie App"}

# def main():
#     # movie_id = input("Enter a movie ID to begin: ")
#     response = get_or_fetch_movie(movie_id=1013850)
#     pprint(response)
#     
# if __name__ == "__main__":
#     main()
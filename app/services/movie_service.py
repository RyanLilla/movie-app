from pprint import pprint
from app.db.models import Movie
from app.external.api_client import fetch_movie_details_safe
from app.repositories import movie_repository

def get_or_fetch_movie(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)
    if movie:
        # pprint(movie)
        return movie

    api_data = fetch_movie_details_safe(movie_id)
    movie = Movie(
        id=api_data["id"],
        title=api_data["title"],
        overview=api_data.get("overview"),
        release_date=api_data.get("release_date"),
        popularity=api_data.get("popularity"),
        vote_average=api_data.get("vote_average"),
        vote_count=api_data.get("vote_count"),
        genre_ids=str(api_data.get("genre_ids"))  # store list as string
    )
    return movie_repository.insert_movie(movie)
    # print(f"Movie not found. Calling TMDB's API instead.\n{api_data.json()}")
    
def get_all_movies_from_db():
    movies = movie_repository.get_all_movies()
    if movies:
        return movies
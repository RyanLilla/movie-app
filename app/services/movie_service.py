from pprint import pprint
from app.db.models import Movie
from app.external import api_client
from app.repositories import movie_repository


def get_watched_movie_by_id(movie_id: int):
    """
    Retrieve a movie by its ID.

    This function first attempts to fetch the movie from the local database.
    If the movie is not found, it fetches the movie details from an external API,
    creates a new Movie object, and inserts it into the database.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        Movie: The movie object retrieved from the database or created from the API data.
    """
    movie = movie_repository.get_movie_by_id(movie_id)
    if movie:
        # pprint(movie)
        return movie

    api_data = api_client.fetch_movie_details_safe(movie_id)
    
    if api_data:
        movie = Movie(
            id=api_data["id"],
            title=api_data["title"],
            overview=api_data.get("overview"),
            release_date=api_data.get("release_date"),
            popularity=api_data.get("popularity"),
            vote_average=api_data.get("vote_average"),
            vote_count=api_data.get("vote_count"),
            genre_ids=str(api_data.get("genre_ids")),
            poster_url=f"https://image.tmdb.org/t/p/original{api_data.get('poster_path')}",
            backdrop_url=f"https://image.tmdb.org/t/p/original{api_data.get('backdrop_path')}"
        )
        return movie
        # return save_watched_movie_to_database(movie)
    
    return None

def search_movie_by_title(query: str):
    # movie = movie_repository.get_movie_by_title(query)
    # if movie:
    #     return movie
    
    api_data = api_client.search_movie_by_query(query=query)
    if api_data:
        movie_list = []
        for movie_item in api_data:
            movie = Movie(
                id=movie_item["id"],
                title=movie_item["title"],
                overview=movie_item.get("overview"),
                release_date=movie_item.get("release_date"),
                popularity=movie_item.get("popularity"),
                vote_average=movie_item.get("vote_average"),
                vote_count=movie_item.get("vote_count"),
                genre_ids=str(movie_item.get("genre_ids")),
                poster_url=f"https://image.tmdb.org/t/p/original{movie_item.get('poster_path')}",
                backdrop_url=f"https://image.tmdb.org/t/p/original{movie_item.get('backdrop_path')}"
            )
            # pprint(movie)
            movie_list.append(movie)
        return movie_list
    return None

def save_watched_movie_to_database(movie):
    return movie_repository.insert_movie(movie)
    
def get_all_watched_movies_from_db():
    """
    Retrieve all movies from the local database.

    Returns:
        list[Movie]: A list of Movie objects retrieved from the database.
                     Returns an empty list if no movies are found.
    """
    movies = movie_repository.get_all_movies()
    if movies:
        return movies

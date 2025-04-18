from pprint import pprint
from app.db.models import Movie
from app.db.schemas import MovieResponse, GenreResponse
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
        genres = movie_repository.get_genres_for_movie(movie.id)
        movie.genres = genres
        return movie

    api_data = api_client.fetch_movie_details_safe(movie_id)
    
    if api_data:
        movie = Movie(
            id=api_data["id"],
            title=api_data["title"],
            overview=api_data["overview"],
            release_date=api_data["release_date"],
            vote_average=int(api_data["vote_average"]),
            vote_count=api_data["vote_count"],
            popularity=int(api_data["popularity"]),
            poster_url=f"https://image.tmdb.org/t/p/original{api_data.get('poster_path')}",
            backdrop_url=f"https://image.tmdb.org/t/p/original{api_data.get('backdrop_path')}",
            adult=api_data["adult"],
            budget=api_data["budget"],
            homepage=api_data["homepage"],
            imdb_id=api_data["imdb_id"],
            original_language=api_data["original_language"],
            original_title=api_data["original_title"],
            revenue=api_data["revenue"],
            runtime=api_data["runtime"],
            status=api_data["status"],
            tagline=api_data["tagline"],
            video=api_data["video"]
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
            if movie_item.get("original_language") != "en":
                continue
            
            movie = Movie(
                id=movie_item["id"],
                title=movie_item["title"],
                overview=movie_item.get("overview"),
                release_date=movie_item.get("release_date"),
                popularity=movie_item.get("popularity"),
                vote_average=movie_item.get("vote_average"),
                vote_count=movie_item.get("vote_count"),
                poster_url=f"https://image.tmdb.org/t/p/original{movie_item.get('poster_path')}",
                backdrop_url=f"https://image.tmdb.org/t/p/original{movie_item.get('backdrop_path')}"
            )
            # pprint(movie_item)
            movie_list.append(movie)
        return movie_list
    return None

def save_watched_movie_to_database(movie):
    return movie_repository.insert_movie(movie)
    
def get_all_watched_movies_from_db() -> list[MovieResponse]:
    """
    Retrieve all movies from the local database as MovieResponse objects.

    Returns:
        list[MovieResponse]: A list of MovieResponse objects retrieved from the database.
    """
    movies = movie_repository.get_all_movies()
    movie_responses: list[MovieResponse] = []

    for movie in movies:
        genres = movie_repository.get_genres_for_movie(movie.id)
        genre_responses = [GenreResponse(id=g.id, name=g.name) for g in genres]

        movie_response = MovieResponse(
            id=movie.id,
            title=movie.title,
            overview=movie.overview,
            release_date=movie.release_date,
            poster_url=movie.poster_url,
            backdrop_url=movie.backdrop_url,
            popularity=movie.popularity,
            vote_average=movie.vote_average,
            vote_count=movie.vote_count,
            genres=genre_responses
        )

        movie_responses.append(movie_response)

    return movie_responses

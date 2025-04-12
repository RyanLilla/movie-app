from turtle import up
from app.db.models import Movie
from app.db.database import get_session
from app.external.api_client import fetch_movie_details_safe
from sqlmodel import select  # Import the select function

class MovieUtils:
    @staticmethod
    def update_movie_urls():
        """
        Update the `poster_url` and `backdrop_url` for each movie in the database
        by fetching the movie details using its `id`.
        """
        with get_session() as session:
            # Use select() to query all movies
            movies = session.exec(select(Movie)).all()
            count = 0
            updates_count = 0
            for movie in movies:
                count += 1
                movie_data = fetch_movie_details_safe(movie.id)
                if movie_data:
                    updates_count += 1
                    if movie_data.get("poster_path") and movie_data.get("backdrop_path"):
                        movie.poster_url = f"https://image.tmdb.org/t/p/original{movie_data.get('poster_path')}"
                        movie.backdrop_url = f"https://image.tmdb.org/t/p/original{movie_data.get('backdrop_path')}"
                        session.add(movie)
                        # session.commit()
                        print(f"Updating movie: {movie.title}")
                    else:
                        # print(f"No poster or backdrop found for movie: {movie.title}")
                        movie.poster_url = ""
                        movie.backdrop_url = ""
                        session.add(movie)
                        # session.commit()
                else:
                    print(f"Movie data not found for ID: {movie.id}")
            session.commit()
            print(f"Total movies processed: {count}")
            print(f"Total movies updated: {updates_count}")
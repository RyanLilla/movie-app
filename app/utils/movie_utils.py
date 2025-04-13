from turtle import up
from app.db.models import Genre, Movie, MovieGenreLink, MovieProductionCompanyLink, ProductionCompany
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


    @staticmethod
    def bulk_add_movies_by_movie_ids(movie_ids):
        """
        Bulk add movies to the database by their IDs.
        
        Args:
            movie_ids (list): List of movie IDs to add.
        """
        with get_session() as session:
            for movie_id in movie_ids:
                api_data = fetch_movie_details_safe(movie_id)
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
                    session.merge(movie)
                    
                    for genre_info in api_data["genres"]:
                        genre = Genre(id=genre_info["id"], name=genre_info["name"])
                        session.merge(genre)

                        link = MovieGenreLink(
                            movie_id=api_data["id"],
                            genre_id=genre_info["id"]
                        )
                        session.merge(link)  # merge ensures we don’t duplicate links
                        
                    for prod_company_info in api_data["production_companies"]:
                        prod_company = ProductionCompany(
                            id=prod_company_info["id"],
                            name=prod_company_info["name"],
                            logo_path=prod_company_info.get("logo_path"),
                            origin_country=prod_company_info.get("origin_country")
                        )
                        session.merge(prod_company)

                        link = MovieProductionCompanyLink(
                            movie_id=api_data["id"],
                            company_id=prod_company_info["id"]
                        )
                        session.merge(link)
                        
            session.commit()

            print(f"Bulk added {len(movie_ids)} movies to the database.")

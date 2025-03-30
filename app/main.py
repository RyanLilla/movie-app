from pprint import pprint
from fastapi import FastAPI

from services.movie_service import get_or_fetch_movie

# app = FastAPI()


def main():
    # movie_id = input("Enter a movie ID to begin: ")
    response = get_or_fetch_movie(movie_id=1013850)
    pprint(response)
    
if __name__ == "__main__":
    main()
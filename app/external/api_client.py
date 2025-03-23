from urllib import response
import requests
from pprint import pprint


# Configurations
BASE_URL = "https://api.themoviedb.org/3"
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNzFlOWNkMDgyMzgxM2UwNTUzNmVhY2M1ODc3ZDk3NCIsIm5iZiI6MTc0MDk1NzQwNC42NTYsInN1YiI6IjY3YzRlNmRjZmRlZDNiNTE2ZjkxZGY2MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9pTT1k7D_NvO5NFjAAVeBC52BAiUHWCTWECxZ-0relI"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def fetch_movie_details(movie_id: int):
    """
    Fetch movie details from TMDB API using the given movie ID.
    """
    url = f"{BASE_URL}/movie/{movie_id}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the movie metadata as JSON
    else:
        print(f"Error: Unable to fetch movie with ID {movie_id}")
        return None

def search_movie_by_query(query: str|None):
    """
    Search for movies by their original, translated and alternative titles.

    Args:
        query (str | None): The title of the movie to search for.
    """
    if not query:
        query = "The Gorge"
        
    url = f"{BASE_URL}/search/movie?query={query}&include_adult=false&language=en-US&page=1"

    response = requests.get(url, headers=headers).json()
    results = response['results'][0]
    # pprint(results)
    return results
    
def fetch_trending_movies():
    """
    Get the current top 10 trending movies for the week.
    """
    url = f"{BASE_URL}/trending/movie/week"
    
    response = requests.get(url, headers=headers).json()
    results = response['results'][:10]
    pprint(results)

def fetch_movie_details_safe(movie_id: int):
    """
    Fetch movie details, returning an empty dict instead of None if failed.
    """
    data = fetch_movie_details(movie_id)
    return data or {}

def fetch_multiple_movies(movie_ids: list[int]):
    """
    Fetch details for multiple movies given a list of IDs.
    """
    movies = []
    for movie_id in movie_ids:
        movie_data = fetch_movie_details_safe(movie_id)
        if movie_data:
            movies.append(movie_data)
    return movies

def fetch_popular_movies(page: int = 1):
    """
    Fetch popular movies (useful for browsing interfaces).
    """
    url = f"{BASE_URL}/movie/popular?language=en-US&page={page}"
    response = requests.get(url, headers=headers).json()
    return response.get('results', [])

import time

def make_request_with_retry(url: str, retries: int = 3, delay: float = 1.0):
    """
    Perform a GET request with retries if the server responds with errors.
    """
    for attempt in range(retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Attempt {attempt + 1} failed (status: {response.status_code}). Retrying...")
            time.sleep(delay)
    print("All attempts failed.")
    return None
import pytest
from unittest.mock import patch, MagicMock
from services.movie_service import get_movie_by_id
from db.models import Movie

@pytest.fixture
def mock_movie():
    return Movie(
        id=1,
        title="Inception",
        overview="A mind-bending thriller.",
        release_date="2010-07-16",
        popularity=90,
        vote_average=8.8,
        vote_count=20000,
        genre_ids="28,12,878"  # Action, Adventure, Sci-Fi
    )

@patch("repositories.movie_repository.get_movie_by_id")
@patch("external.api_client.fetch_movie_details_safe")
@patch("repositories.movie_repository.insert_movie")
def test_get_or_fetch_movie_returns_existing_movie(
    mock_insert_movie, mock_fetch_movie_details_safe, mock_get_movie_by_id, mock_movie
):
    """Test when a movie exists in the database, it is returned without calling the API."""
    
    mock_get_movie_by_id.return_value = mock_movie  # Movie found in DB

    movie = get_movie_by_id(1)

    assert movie.id == mock_movie.id
    assert movie.title == "Inception"
    mock_get_movie_by_id.assert_called_once()
    mock_fetch_movie_details_safe.assert_not_called()
    mock_insert_movie.assert_not_called()

@patch("app.repositories.movie_repository.get_movie_by_id")
@patch("app.external.api_client.fetch_movie_details_safe")
@patch("app.repositories.movie_repository.insert_movie")
def test_get_or_fetch_movie_fetches_from_api_and_saves(
    mock_insert_movie, mock_fetch_movie_details_safe, mock_get_movie_by_id
):
    """Test when a movie is NOT in the DB, it is fetched from the API and stored."""
    
    mock_get_movie_by_id.return_value = None  # Movie not in DB
    mock_api_data = {
        "id": 1,
        "title": "Inception",
        "overview": "A mind-bending thriller.",
        "release_date": "2010-07-16",
        "popularity": 90,
        "vote_average": 8.8,
        "vote_count": 20000,
        "genre_ids": [28, 12, 878]  # Action, Adventure, Sci-Fi
    }
    
    mock_fetch_movie_details_safe.return_value = mock_api_data
    mock_insert_movie.return_value = Movie(**mock_api_data)

    movie = get_movie_by_id(1)

    assert movie.id == 1
    assert movie.title == "Inception"
    mock_get_movie_by_id.assert_called_once()
    mock_fetch_movie_details_safe.assert_called_once_with(1)
    mock_insert_movie.assert_called_once()
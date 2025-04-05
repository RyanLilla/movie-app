import { useState } from "react";
import { fetchMovieByTitle } from "../services/movieService";
import type { Movie } from "../types/index";
import "./css/SearchMovie.css";

const SearchMovie = () => {
  const [query, setQuery] = useState("");
  const [movies, setMovies] = useState<Movie[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setError("");
    try {
        const results = await fetchMovieByTitle(query);
        setMovies([results]);
    } catch (error) {
        console.error("Error fetching movie:", error);
        setError(`Failed to fetch movie: ${query}. Please try again.`);
    } finally {
        setLoading(false);
    }
  };

  return (
    <div className="search-container">
      <h2 className="search-heading">Search for a Movie</h2>
      <div className="search-controls">
        <input
          type="text"
          placeholder="Enter movie title"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="search-input"
        />
        <button
          onClick={handleSearch}
          className="search-button"
        >
          Search
        </button>
      </div>

      {loading && <p>Loading...</p>}
      {error && <p className="search-error">{error}</p>}

      {movies.length > 0 && (
        <div className="movie-card">
          <h3 className="movie-title">{movies[0].title}</h3>
          {movies[0].poster_url && (
            <img
              src={movies[0].poster_url}
              alt={`${movies[0].title} Poster`}
              className="poster"
            />
          )}
          <p className="movie-release">Released: {movies[0].release_date}</p>
          <p>{movies[0].overview}</p>
        </div>
      )}
    </div>
  );
};

export default SearchMovie;
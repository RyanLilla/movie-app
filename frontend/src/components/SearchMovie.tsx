import { useState } from "react";
import { fetchMovieByTitle } from "../services/movieService";
import type { Movie } from "../types/index";
import MovieSearchBar from "./MovieSearchBar";
import "./css/SearchMovie.css";


type MovieReponse = Pick<Movie, "id" | "title" | "poster_url" | "release_date">;

const SearchMovie = () => {
  const [movies, setMovies] = useState<MovieReponse[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async (query: string) => {
    if (!query.trim()) return;

    setLoading(true);
    setError("");
    try {
        const results = await fetchMovieByTitle(query);
        setMovies(results);
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
      <MovieSearchBar onSearch={handleSearch} />

      {loading && <p>Loading...</p>}
      {error && <p className="search-error">{error}</p>}

      {movies.length > 0 && (
        <div className="movies-grid">
          {movies.map((movie) => (
            <div key={movie.id} className="movie-card">
              <h3 className="movie-title">{movie.title}</h3>
              {movie.poster_url && (
                <img
                  src={movie.poster_url}
                  alt={`${movie.title} Poster`}
                  className="poster"
                />
              )}
              <p className="movie-release">Released: {movie.release_date}</p>
              {/* <p>{movie.overview}</p> */}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default SearchMovie;
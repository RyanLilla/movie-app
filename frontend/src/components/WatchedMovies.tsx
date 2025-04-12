import { useState, useEffect } from "react";
import { fetchWatchedMovies } from "../services/movieService";
import type { Movie } from "../types/index";
import "./css/SearchMovie.css";

const WatchedMovies = () => {
  const [movies, setMovies] = useState<Movie[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const getMovies = async () => {
      setLoading(true);
      setError("");
      try {
        const results = await fetchWatchedMovies();
        setMovies(results);
      } catch (error) {
        console.error("Error fetching watched movies:", error);
        setError("Failed to load watched movies.");
      } finally {
        setLoading(false);
      }
    };

    getMovies();
  }, []);

  return (
    <div className="search-container">
      <h2 className="search-heading">Watched Movies</h2>

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
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default WatchedMovies;
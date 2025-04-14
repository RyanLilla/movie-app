import { useState, useEffect } from "react";
import { fetchWatchedMovies } from "../services/movieService";
import type { Movie, Genre } from "../types/index";
import "./css/SearchMovie.css";

const WatchedMovies = () => {
  const [movies, setMovies] = useState<Movie[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [selectedGenre, setSelectedGenre] = useState<string | null>(null);

  const uniqueGenres = Array.from(
    new Set(movies.flatMap((movie) => movie.genres.map((g) => g.name)))
  );

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

  const filteredMovies = selectedGenre
    ? movies.filter((movie) =>
        movie.genres.some((genre) => genre.name === selectedGenre)
      )
    : movies;

  return (
    <div className="search-container">
      <h2 className="search-heading">Watched</h2>

      {loading && <p>Loading...</p>}
      {error && <p className="search-error">{error}</p>}

      <select
        value={selectedGenre ?? ""}
        onChange={(e) => setSelectedGenre(e.target.value || null)}
        className="genre-filter"
      >
        <option value="">All Genres</option>
        {uniqueGenres.map((genre) => (
            <option key={genre} value={genre}>
                {genre}
            </option>
        ))}
      </select>

      {filteredMovies.length > 0 && (
        <div className="movies-grid">
          {filteredMovies.map((movie) => (
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
              {movie.genres && movie.genres.length > 0 && (
                <p className="movie-genres">
                  {movie.genres.map((genre) => genre.name).join(", ")}
                </p>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default WatchedMovies;
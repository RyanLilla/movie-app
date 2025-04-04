import { useState } from "react";
import { fetchMovieById } from "../services/movieService";

const MovieDetails = () => {
  const [movieId, setMovieId] = useState<number>(1013850); // Example movie ID
  const [movie, setMovie] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFetchMovie = async () => {
    setLoading(true);
    setError(null);

    try {
      const movieData = await fetchMovieById(movieId);
      setMovie(movieData);
    } catch (error) {
      console.error("Error fetching movie:", error);
      setError("Failed to fetch movie details. Please try again.");
    }

    setLoading(false);
  };

  return (
    <div>
      <h2>Fetch Movie Details</h2>
      <input
        type="number"
        value={movieId}
        onChange={(e) => setMovieId(Number(e.target.value))}
        placeholder="Enter Movie ID"
      />
      <button onClick={handleFetchMovie}>Get Movie</button>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {movie && (
        <div>
          <h3>{movie.title}</h3>
          <p>{movie.overview}</p>
          <p>Released: {movie.release_date}</p>
        </div>
      )}
    </div>
  );
};

export default MovieDetails;
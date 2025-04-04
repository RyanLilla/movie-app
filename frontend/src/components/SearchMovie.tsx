import { useState } from "react";
import { fetchMovieByTitle } from "../services/movieService";
import type { Movie } from "../types/index";

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
        setError("Failed to fetch movie: {query}. Please try again.");
    } finally {
        setLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h2 className="text-xl font-semibold mb-4">Search for a Movie</h2>
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="Enter movie title"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="border px-2 py-1 flex-grow rounded"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-600 text-white px-4 py-1 rounded hover:bg-blue-700"
        >
          Search
        </button>
      </div>

      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {movies.length > 0 && (
        <div className="border p-3 rounded shadow">
          <h3 className="font-bold">{movies[0].title}</h3>
          <p className="text-sm text-gray-600">Released: {movies[0].release_date}</p>
          <p>{movies[0].overview}</p>
        </div>
      )}
    </div>
  );
};

export default SearchMovie;
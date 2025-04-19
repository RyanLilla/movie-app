import { useState } from "react";
import "./css/SearchMovie.css";

interface MovieSearchBarProps {
  onSearch: (query: string) => void;
}

const MovieSearchBar = ({ onSearch }: MovieSearchBarProps) => {
  const [query, setQuery] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query);
    }
  };

  return (
    <form className="search-controls" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter movie title"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="search-input"
      />
      <button type="submit" className="search-button">
        Search
      </button>
    </form>
  );
};

export default MovieSearchBar;
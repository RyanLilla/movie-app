import axios from "axios";

// Get the API base URL from the .env file
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// Define an interface for movie data
interface Movie {
  id: number;
  title: string;
  overview: string;
  release_date: string;
  popularity: number;
  vote_average: number;
  vote_count: number;
  genre_ids: number[];
  poster_url: string;
  backdrop_url: string;
}

// Function to fetch a movie by ID
export const fetchMovieById = async (movieId: number): Promise<Movie> => {
  try {
    const response = await axios.get<Movie>(`${API_BASE_URL}/movie/${movieId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching movie by ID:", error);
    throw error;
  }
};

// Function to fetch a movie by title
export const fetchMovieByTitle = async (title: string): Promise<Movie[]> => {
  try {
    const response = await axios.get<Movie[]>(`${API_BASE_URL}/search/movie`, {
      params: { query: title },
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching movie by title:", error);
    throw error;
  }
};

// Function to fetch all watched movies from the database
export const fetchWatchedMovies = async (): Promise<Movie[]> => {
  try {
    const response = await axios.get<Movie[]>(`${API_BASE_URL}/movies/all`);
    return response.data;
  } catch (error) {
    console.error("Error fetching watched movies:", error);
    throw error;
  }
};
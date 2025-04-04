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
}

// Function to fetch a movie by ID
export const fetchMovieById = async (movieId: number): Promise<Movie> => {
  try {
    const response = await axios.get<Movie>(`${API_BASE_URL}/movies/${movieId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching movie:", error);
    throw error;
  }
};
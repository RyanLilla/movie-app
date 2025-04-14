// frontend/src/types/index.ts

export interface Genre {
  id: number;
  name: string;
}
  
export interface Movie {
  id: number;
  title: string;
  overview: string;
  release_date: string;
  popularity: number;
  vote_average: number;
  vote_count: number;
  genres: Genre[];
  poster_url: string;
  backdrop_url: string;
}
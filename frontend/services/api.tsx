
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export interface SearchResult {
  index: number;
  label: string;
  similarity: number;
  image_url: string;
}

export interface SearchResponse {
  results: SearchResult[];
}

export async function searchImage(file: File): Promise<SearchResult[]> {
  const formData = new FormData();

  formData.append("file", file);

  const response = await axios.post<SearchResponse>(
    `${API_URL}/search`,
    formData
  );

  return response.data.results;
}


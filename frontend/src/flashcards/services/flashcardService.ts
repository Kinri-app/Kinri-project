import axios from "axios";
import type { Flashcard } from "../types/flashcardTypes.ts";

const API_URL = "http://localhost:5000/api";

export const fetchFlashcards = async (): Promise<Flashcard[]> => {
    const response = await axios.get<Flashcard[]>(`${API_URL}/flashcards/`);
    return response.data;
};

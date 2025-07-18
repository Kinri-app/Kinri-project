import axios from "axios";
import type { Flashcard } from "../types/flashcardType";

const API_URL = "http://localhost:5000/api";

export const fetchFlashcards = async (): Promise<Flashcard[]> => {
    const response = await axios.get<Flashcard[]>(`${API_URL}/flashcards/`);
    console.log(response.data);
    return response.data;
};

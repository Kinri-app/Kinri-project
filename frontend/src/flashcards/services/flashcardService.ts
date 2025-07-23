import axios from "axios";
import type { Flashcard } from "../types/flashcardType";

const API_URL = "http://localhost:5000/api";

export const fetchFlashcards = async (): Promise<Flashcard[]> => {
    const { data } = await axios.get(`${API_URL}/flashcards/`);

    return data.data;
};

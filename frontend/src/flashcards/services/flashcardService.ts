import axios from "axios";
import type { Flashcard } from "../types/flashcardType";
import { API_URL } from "../../api/apiUrl";


export const fetchFlashcards = async (): Promise<Flashcard[]> => {
    const { data } = await axios.get(`${API_URL}/flashcards/`);

    return data.data;
};

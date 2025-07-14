import { create } from "zustand";
import { fetchFlashcards } from "../services/flashcardService.ts";
import type { Flashcard } from "../types/flashcardTypes.ts";

interface FlashcardState {
    flashcards: Flashcard[];
    loading: boolean;
    error: string | null;
    loadFlashcards: () => Promise<void>;
}

export const useFlashcardStore = create<FlashcardState>((set) => ({
    flashcards: [],
    loading: false,
    error: null,
    loadFlashcards: async () => {
        set({ loading: true, error: null });
        try {
            const data = await fetchFlashcards();
            set({ flashcards: data, loading: false });
        } catch (err: any) {
            set({ error: err.message ?? "Failed to load flashcards", loading: false });
        }
    },
}));

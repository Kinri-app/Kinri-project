import { create } from "zustand";
import {
    evaluateAssessmentWithAI,
    sendMessageToAI,
} from "../services/chatService.ts";
import type { AIChatMessage } from "../types/chatTypes.ts";
import type { AssessmentResponseItem } from "../../assessments/types/assessmentTypes.ts";

interface ChatState {
    chatHistory: AIChatMessage[];
    loading: boolean;
    error: string | null;
    sendMessage: (message: string) => Promise<void>;
    evaluateAssessment: (
        assessmentResponseItems: AssessmentResponseItem[]
    ) => void;
    setChatHistory: (chatHistory: AIChatMessage[]) => void;
    resetChat: () => void;
}

export const useChatStore = create<ChatState>((set, get) => ({
    chatHistory: [],
    loading: false,
    error: null,

    sendMessage: async (message: string) => {
        const { chatHistory } = get();
        set({ loading: true, error: null });

        try {
            const { history } = await sendMessageToAI(message, chatHistory);
            set({
                chatHistory: history,
                loading: false,
            });
        } catch (err: any) {
            set({ error: err.message, loading: false });
        }
    },
    evaluateAssessment: async (
        assessmentResponseItems: AssessmentResponseItem[]
    ) => {
        set({ loading: true, error: null });

        try {
            const { history } = await evaluateAssessmentWithAI(
                assessmentResponseItems
            );

            set({
                chatHistory: history,
                loading: false,
            });
        } catch (err: any) {
            set({ error: err.message, loading: false });
        }
    },
    setChatHistory: async (chatHistory: AIChatMessage[]) => {
        set({ chatHistory });
    },
    resetChat: () => set({ chatHistory: [], error: null }),
}));

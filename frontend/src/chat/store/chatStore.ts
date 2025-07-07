import {create} from 'zustand';
import {sendMessageToAI} from "../services/chatService.ts";
import type {AIChatMessage} from "../types/chatTypes.ts";

interface ChatState {
    chatHistory: AIChatMessage[];
    loading: boolean;
    error: string | null;
    sendMessage: (message: string) => Promise<void>;
    resetChat: () => void;
}

export const useChatStore = create<ChatState>((set, get) => ({
    chatHistory: [],
    loading: false,
    error: null,

    sendMessage: async (message: string) => {
        const {chatHistory} = get();
        set({loading: true, error: null});

        try {
            const data = await sendMessageToAI(message, chatHistory);
            set({chatHistory: data.chat_history, loading: false});
        } catch (err: any) {
            set({error: err.message, loading: false});
        }
    },

    resetChat: () => set({chatHistory: [], error: null})
}));

import {create} from "zustand";
import {nanoid} from "nanoid";
import type {Message} from "../chatTypes.ts";

interface ChatState {
    messages: Message[];
    sendMessage: (text: string) => void;
}

export const useChatStore = create<ChatState>((set) => ({
    messages: [],
    sendMessage: (text) => {
        const userMsg: Message = {
            id: nanoid(),
            text,
            sender: "user",
        };
        const aiMsg: Message = {
            id: nanoid(),
            text: "This is a placeholder response from the AI.",
            sender: "ai",
        };

        set((state) => ({
            messages: [...state.messages, userMsg, aiMsg],
        }));
    },
}));

export interface AIChatMessage {
    role: 'user' | 'assistant';
    content: string;
}

export interface ChatResponseData {
    reply: string;
    chat_history: AIChatMessage[];
}
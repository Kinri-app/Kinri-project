export interface AIChatMessage {
    role: 'user' | 'assistant';
    content: string;
}

export interface ChatResponseData {
    reply: string;
    history: AIChatMessage[];
}
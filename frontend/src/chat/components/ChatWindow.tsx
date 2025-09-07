import { useRef, useEffect } from "react";
import ChatMessage from "./ChatMessage";
import type { AIChatMessage } from "../types/chatTypes";

interface ChatWindowProps {
    chatHistory: AIChatMessage[]
}


export const ChatWindow = ({ chatHistory }: ChatWindowProps) => {
    const chatContainerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
    }, [chatHistory]);

    return (
        <div
            ref={chatContainerRef}
            className="flex-1 overflow-y-auto px-6 py-4 space-y-4"
        >
            {chatHistory.map((msg, i) => (
                <ChatMessage key={i} role={msg.role} content={msg.content} />
            ))}
        </div>
    );
};

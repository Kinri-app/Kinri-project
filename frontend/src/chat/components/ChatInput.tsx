import { useState } from "react";
import { useChatStore } from "../store/chatStore.ts";
import { PaperAirplaneIcon } from "@heroicons/react/16/solid";

const ChatInput = () => {
    const [message, setMessage] = useState("");
    const { sendMessage, loading } = useChatStore();

    const handleSend = async (e: { preventDefault: () => void; }) => {
        e.preventDefault();
        if (!message.trim()) return;
        await sendMessage(message);
        setMessage('');
    };

    return (
        <form onSubmit={handleSend} className="flex items-center space-x-2">
            <input
                className={`flex h-10 w-full rounded-md border px-3 py-2 text-sm text-gray-800 focus:outline-none transition
      ${loading
                        ? 'border-gray-200 bg-gray-100 cursor-not-allowed opacity-60'
                        : 'border-gray-300 focus:ring-2 focus:ring-gray-300'
                    }`}
                placeholder={loading ? "Loading..." : "Type your message"}
                value={message}
                disabled={loading}
                onChange={(e) => setMessage(e.target.value)}
            />

            <button
                type="submit"
                disabled={loading}
                className={`h-10 px-3 py-2 rounded-md text-sm font-medium text-white transition cursor-pointer
      ${loading
                        ? 'bg-gray-400 cursor-not-allowed'
                        : 'bg-kinri-primary hover:bg-yellow-700 active:bg-yellow-700'
                    }`}
            >
                {loading ? (
                    <div
                        className="animate-spin h-5 w-5 border-2 border-white border-t-transparent rounded-full mx-auto" />
                ) : (
                    <PaperAirplaneIcon className="w-5 h-5" />
                )}
            </button>
        </form>
    );
};

export default ChatInput;

import {useState} from "react";
import {useChatStore} from "../store/chatStore.ts";
import {PaperAirplaneIcon} from "@heroicons/react/16/solid";

const ChatInput = () => {
    const [message, setMessage] = useState("");
    const sendMessage = useChatStore((state) => state.sendMessage);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (!message.trim()) return;
        sendMessage(message);
        setMessage("");
    };

    return (
        <form onSubmit={handleSubmit} className="flex items-center space-x-2">
            <input
                className="flex h-10 w-full rounded-md border border-gray-300 px-3 py-2 text-sm text-gray-800 focus:outline-none focus:ring-2 focus:ring-gray-300"
                placeholder="Type your message"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <button
                type="submit"
                className=" border border-yellow-600 text-yellow-600 h-10 px-3 py-2 focus:outline-none rounded-md cursor-pointer hover:bg-yellow-600 hover:text-white
             active:bg-yellow-400 transition font-medium"
            >
                <PaperAirplaneIcon className="w-5 h-5"/>
            </button>
        </form>
    );
};

export default ChatInput;

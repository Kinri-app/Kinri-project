import ChatInput from "./ChatInput";
import {useChatStore} from "../store/chatStore.ts";
import ChatMessage from "./ChatMessage";

const ChatBox = () => {
    const {chatHistory,error} = useChatStore();


    return (
        <div className="flex flex-col border border-gray-200 rounded-lg shadow-sm bg-white h-[600px]">
            <h2 className="text-red-500">{error}</h2>

            {/* Header section */}
            <div className="px-6 py-4 border-b border-b-gray-200">
                <h2 className="text-lg font-semibold text-gray-900">Echo AI</h2>
                <p className="text-sm text-gray-500">Powered by Mistral</p>
            </div>

            {/* Chat messages section */}
            <div className="flex-1 overflow-y-auto px-6 py-4 space-y-4">
                {chatHistory.map((msg, i) => (
                    <ChatMessage key={i} role={msg.role} content={msg.content}/>
                ))}
            </div>

            {/* Input section */}
            <div className="px-6 py-4 border-t border-t-gray-200">
                <ChatInput/>
            </div>
        </div>
    );
};

export default ChatBox;

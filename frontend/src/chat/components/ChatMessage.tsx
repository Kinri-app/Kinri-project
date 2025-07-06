import type {Message} from "../chatTypes.ts";

type ChatMessageProps = Omit<Message, "id">

const ChatMessage = ({sender, text}: ChatMessageProps) => {
    const isUser = sender === "user";

    return (
        <div className={`w-[100%] flex gap-3 text-sm ${isUser ? "justify-end" : "justify-start"}`}>
            <div className="bg-gray-50 px-4 py-2 rounded-lg shadow-sm break-words max-w-[80%]">
                <p className="font-medium text-gray-800">{isUser ? "You" : "Echo"}</p>
                <p className="text-gray-700">{text}</p>
            </div>
        </div>
    );
};

export default ChatMessage;

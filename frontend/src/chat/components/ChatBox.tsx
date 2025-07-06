import {useEffect} from "react";
import ChatInput from "./ChatInput";
import ChatMessage from "./ChatMessage";
import {useChatStore} from "../store/chatStore.ts";
import {useAssessmentStore} from "../../assessments/store/assessmentStore.ts";

const ChatBox = () => {
    const messages = useChatStore((state) => state.messages);
    const responses = useAssessmentStore((state) => state.responses); // ✅ Access stored survey responses

    useEffect(() => {
        if (responses) {
            console.log("Assessment responses:", responses);

            // Example: you can use this to send the data to your API or generate a dynamic message
            // const summary = responses.map(r => `${r.id}: ${r.score}`).join(", ");
            // sendMessage({ sender: 'system', text: `Survey completed. Scores: ${summary}` });
        }
    }, [responses]);

    return (
        <div className="flex flex-col border border-gray-200 rounded-lg shadow-sm bg-white h-[600px]">
            {/* Header section */}
            <div className="px-6 py-4 border-b border-b-gray-200">
                <h2 className="text-lg font-semibold text-gray-900">Echo AI</h2>
                <p className="text-sm text-gray-500">Powered by Mistral</p>
            </div>

            {/* Chat messages section */}
            <div className="flex-1 overflow-y-auto px-6 py-4 space-y-4">
                {messages.map((msg) => (
                    <ChatMessage key={msg.id} sender={msg.sender} text={msg.text}/>
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

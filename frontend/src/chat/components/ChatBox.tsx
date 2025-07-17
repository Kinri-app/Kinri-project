import ChatInput from "./ChatInput";
import { useChatStore } from "../store/chatStore.ts";
import ChatMessage from "./ChatMessage";
import { useEffect } from "react";
import { useAssessmentStore } from "../../assessments/store/assessmentStore.ts";
import { useAuth0 } from "@auth0/auth0-react";

const welcomeMessage = `
Hi there, and welcome. I'm really glad you're here.

You don’t need to have taken an assessment to talk with me—just showing up is enough. 
I’m here to support you however you need, whether that’s listening, offering insights, or simply being present.

If you’ve been feeling a bit stressed lately, that’s completely okay. 
Stress is a common response to life’s challenges, and you’re not alone in it.

If you’re curious, I can gently share more about how stress affects us—physically, emotionally, and mentally—and 
some ways to manage it. But there’s no pressure. 

Whatever you feel comfortable with, we’ll go at your pace.

How does that sound?
`;


const ChatBox = () => {
    const { chatHistory, setChatHistory, evaluateAssessment, error } = useChatStore();
    const { responses, clearResponses } = useAssessmentStore();
    const { isAuthenticated, getAccessTokenSilently } = useAuth0();
    
    useEffect(() => {
        const fetchAssessmentData = async () => {
            try {
                let token;
                if (isAuthenticated) {
                    token = await getAccessTokenSilently();
                }
                await evaluateAssessment(responses || [], token);
            } catch (error) {
                console.error('Error evaluating assessment:', error);
            }
        }

        if (chatHistory.length === 0 && !responses) {
            setChatHistory([{ role: "assistant", content: welcomeMessage }]);
        } else if (responses) {
            fetchAssessmentData();
            clearResponses();
        }

    }, [chatHistory.length, setChatHistory, responses, clearResponses, evaluateAssessment, isAuthenticated, getAccessTokenSilently]);


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
                    <ChatMessage key={i} role={msg.role} content={msg.content} />
                ))}
            </div>

            {/* Input section */}
            <div className="px-6 py-4 border-t border-t-gray-200">
                <ChatInput />
            </div>
        </div>
    );
};

export default ChatBox;

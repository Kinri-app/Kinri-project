import type {AIChatMessage} from "../types/chatTypes.ts";
import Markdown from "react-markdown"



// const ChatMessage = ({role, content}: AIChatMessage) => {
//     const isUser = role === "user";

//     return (
//         <div className={`w-[100%] flex gap-3 text-sm ${isUser ? "justify-end" : "justify-start"}`}>
//             <div className="bg-gray-50 px-4 py-2 rounded-lg shadow-sm break-words max-w-[80%]">
//                 <p className="font-medium text-gray-800">{isUser ? "You" : "Echo"}</p>
//                 {isUser ? (
//                     <p className="text-gray-700">{content}</p>
//                 ):(
//                     <div className="text-gray-700"><Markdown>
//                         {content}
//                         </Markdown>
//                     </div>
//                 )}
//             </div>
//         </div>
//     );
// };

// export default ChatMessage;


const ChatMessage = ({role, content}: AIChatMessage) => {
    const isUser = role === "user";

    return (
        <div className={`w-[100%] flex gap-3 text-sm ${isUser ? "justify-end" : "justify-start"}`}>
            <div className="bg-gray-50 px-4 py-2 rounded-lg shadow-sm break-words max-w-[80%]">
                <p className="font-medium text-gray-800">{isUser ? "You" : "Echo"}</p>
                <p className="text-gray-700">{content}</p>

            </div>
        </div>
    );
};

export default ChatMessage;

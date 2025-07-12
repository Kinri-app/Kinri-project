import axios from 'axios';
import type {AIChatMessage, ChatResponseData} from "../types/chatTypes.ts";
import type {StandardApiResponse} from "../../types/apiTypes.ts";

const API_URL = "http://localhost:5000/api/chat/";

export const sendMessageToAI = async (
    message: string,
    history: AIChatMessage[] = []
): Promise<ChatResponseData> => {
    try {
        const response = await axios.post<StandardApiResponse>(API_URL, {
            message,
            history
        });

        return response.data.data;
    } catch (error: any) {
        const message =
            error?.response?.data?.developerMessage ||
            error?.response?.data?.message ||
            'Unknown error occurred';
        throw new Error(message);
    }
};

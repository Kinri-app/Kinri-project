import axios from "axios";
import type { AIChatMessage, ChatResponseData } from "../types/chatTypes.ts";
import type { StandardApiResponse } from "../../types/apiTypes.ts";
import type { AssessmentResponseItem } from "../../assessments/types/assessmentTypes.ts";

const API_URL = "http://localhost:5000/api";

export const sendMessageToAI = async (
    message: string,
    history: AIChatMessage[] = []
): Promise<ChatResponseData> => {
    try {
        const response = await axios.post<StandardApiResponse>(
            `${API_URL}/chat/`,
            {
                message,
                history,
            }
        );

        return response.data.data;
    } catch (error: any) {
        const message =
            error?.response?.data?.developerMessage ||
            error?.response?.data?.message ||
            "Unknown error occurred";
        throw new Error(message);
    }
};

export const evaluateAssessmentWithAI = async (
    assessmentResponseItems: AssessmentResponseItem[]
): Promise<ChatResponseData> => {
    try {
        const response = await axios.post<StandardApiResponse>(
            `${API_URL}/assessments/evaluate`,

            assessmentResponseItems
        );

        const { chat_history, reply } = response.data.data;

        chat_history.shift();

        return { reply, chat_history };
    } catch (error: any) {
        const message =
            error?.response?.data?.developerMessage ||
            error?.response?.data?.message ||
            "Unknown error occurred";
        throw new Error(message);
    }
};

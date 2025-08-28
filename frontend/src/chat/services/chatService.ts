import axios from "axios";
import type { AIChatMessage, ChatResponseData } from "../types/chatTypes.ts";
import type { StandardApiResponse } from "../../types/apiTypes.ts";
import type { AnswerItem } from "../../assessments/types/assessmentTypes.ts";

const API_URL = import.meta.env.VITE_API_URL;

export const sendMessageToAI = async (
    message: string,
    history: AIChatMessage[] = [],
    token: string
): Promise<ChatResponseData> => {
    try {
        const response = await axios.post<StandardApiResponse>(
            `${API_URL}/chat/`,
            {
                message,
                history,
            },
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
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
    assessmentResponseItems: AnswerItem[],
    token: string
): Promise<ChatResponseData> => {
    try {
        const response = await axios.post<StandardApiResponse>(
            `${API_URL}/assessments/evaluate`,

            assessmentResponseItems,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }
        );

        const { history, reply } = response.data.data;

        return {
            reply,
            history: history.filter((message) => message.role === "assistant"),
        };
    } catch (error: any) {
        const message =
            error?.response?.data?.developerMessage ||
            error?.response?.data?.message ||
            "Unknown error occurred";
        throw new Error(message);
    }
};

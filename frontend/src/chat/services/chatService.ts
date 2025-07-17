import apiService from "../../services/api";
import type { AIChatMessage, ChatResponseData } from "../types/chatTypes.ts";
import type { StandardApiResponse } from "../../types/apiTypes.ts";
import type { AssessmentResponseItem } from "../../assessments/types/assessmentTypes.ts";

export const sendMessageToAI = async (
    message: string,
    history: AIChatMessage[] = [],
    token?: string
): Promise<ChatResponseData> => {
    try {
        const response = await apiService.post<ChatResponseData>(
            "/chat",
            {
                message,
                history,
            },
            token
        );

        return response.data.data;
    } catch (error: any) {
        const message =
            error?.message ||
            "Unknown error occurred";
        throw new Error(message);
    }
};

export const evaluateAssessmentWithAI = async (
    assessmentResponseItems: AssessmentResponseItem[],
    token?: string
): Promise<ChatResponseData> => {
    try {
        const response = await apiService.post<ChatResponseData>(
            "/assessments/evaluate",
            assessmentResponseItems,
            token
        );

        const { history, reply } = response.data.data;

        return {
            reply,
            history: history.filter((message) => message.role === "assistant"),
        };
    } catch (error: any) {
        const message =
            error?.message ||
            "Unknown error occurred";
        throw new Error(message);
    }
};

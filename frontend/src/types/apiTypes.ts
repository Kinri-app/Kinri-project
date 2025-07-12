import type {ChatResponseData} from "../chat/types/chatTypes.ts";

export interface StandardApiResponse {
    timeStamp: string;
    status: string;
    statusCode: number;
    message: string;
    data: ChatResponseData;
    reason?: string;
    developerMessage?: string;
}
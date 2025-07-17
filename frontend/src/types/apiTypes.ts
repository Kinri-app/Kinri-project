import type {ChatResponseData} from "../chat/types/chatTypes.ts";

export interface StandardApiResponse<T = any> {
    timeStamp: string;
    status: string;
    statusCode: number;
    message: string;
    data: T;
    reason?: string;
    developerMessage?: string;
}

// User-related types
export interface User {
    id: string;
    auth0_id: string;
    email?: string;
    name?: string;
    picture?: string;
    created_at?: string;
    updated_at?: string;
}

export interface UserProfileData {
    user: User;
}

export interface UsersListData {
    users: User[];
}

// Common API response types
export type UserProfileResponse = StandardApiResponse<UserProfileData>;
export type UsersListResponse = StandardApiResponse<UsersListData>;
export type ChatResponse = StandardApiResponse<ChatResponseData>;
import apiService, { ApiError } from './api';
import { UserProfileResponse, UsersListResponse, User } from '../types/apiTypes';

export class UserService {
  /**
   * Get the current user's profile
   */
  async getProfile(token: string): Promise<User> {
    try {
      const response = await apiService.get<{ user: User }>('/users/profile', token);
      return response.data.data.user;
    } catch (error) {
      console.error('Error fetching user profile:', error);
      throw error as ApiError;
    }
  }

  /**
   * Get all users (requires appropriate permissions)
   */
  async getUsers(token: string): Promise<User[]> {
    try {
      const response = await apiService.get<{ users: User[] }>('/users/data', token);
      return response.data.data.users;
    } catch (error) {
      console.error('Error fetching users:', error);
      throw error as ApiError;
    }
  }

  /**
   * Update user profile (if implemented on backend)
   */
  async updateProfile(token: string, userData: Partial<User>): Promise<User> {
    try {
      const response = await apiService.put<{ user: User }>('/users/profile', userData, token);
      return response.data.data.user;
    } catch (error) {
      console.error('Error updating user profile:', error);
      throw error as ApiError;
    }
  }
}

// Export singleton instance
export const userService = new UserService();
export default userService; 
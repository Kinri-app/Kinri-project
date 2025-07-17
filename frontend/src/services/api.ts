import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios';
import { API_CONFIG } from '../config/api';
import { StandardApiResponse } from '../types/apiTypes';

class ApiService {
  private api: AxiosInstance;

  constructor() {
    this.api = axios.create({
      baseURL: API_CONFIG.BASE_URL,
      timeout: API_CONFIG.TIMEOUT,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Request interceptor to add auth token
    this.api.interceptors.request.use(
      (config) => {
        // Token will be added by the calling component that has access to Auth0
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Response interceptor for standardized error handling
    this.api.interceptors.response.use(
      (response: AxiosResponse<StandardApiResponse>) => {
        return response;
      },
      (error: AxiosError) => {
        console.error('API Error:', error);
        return Promise.reject(this.handleError(error));
      }
    );
  }

  private handleError(error: AxiosError): ApiError {
    if (error.response) {
      // Server responded with error status
      return {
        status: error.response.status,
        message: (error.response.data as any)?.message || 'Server error occurred',
        data: error.response.data,
      };
    } else if (error.request) {
      // Request made but no response received
      return {
        status: 0,
        message: 'Network error - unable to reach server',
        data: null,
      };
    } else {
      // Error in request setup
      return {
        status: 0,
        message: error.message || 'Request setup error',
        data: null,
      };
    }
  }

  // Generic request method with token
  async request<T = any>(
    method: 'GET' | 'POST' | 'PUT' | 'DELETE',
    url: string,
    data?: any,
    token?: string
  ): Promise<AxiosResponse<StandardApiResponse<T>>> {
    const headers: any = {};
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }

    return this.api.request({
      method,
      url,
      data,
      headers,
    });
  }

  // Convenience methods
  async get<T = any>(url: string, token?: string): Promise<AxiosResponse<StandardApiResponse<T>>> {
    return this.request<T>('GET', url, undefined, token);
  }

  async post<T = any>(url: string, data?: any, token?: string): Promise<AxiosResponse<StandardApiResponse<T>>> {
    return this.request<T>('POST', url, data, token);
  }

  async put<T = any>(url: string, data?: any, token?: string): Promise<AxiosResponse<StandardApiResponse<T>>> {
    return this.request<T>('PUT', url, data, token);
  }

  async delete<T = any>(url: string, token?: string): Promise<AxiosResponse<StandardApiResponse<T>>> {
    return this.request<T>('DELETE', url, undefined, token);
  }
}

export interface ApiError {
  status: number;
  message: string;
  data: any;
}

// Export singleton instance
export const apiService = new ApiService();
export default apiService; 
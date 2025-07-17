// API Configuration
export const API_CONFIG = {
  BASE_URL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api',
  TIMEOUT: 10000, // 10 seconds
} as const;

// Auth0 Configuration
export const AUTH0_CONFIG = {
  DOMAIN: import.meta.env.VITE_AUTH0_DOMAIN || '',
  CLIENT_ID: import.meta.env.VITE_AUTH0_CLIENT_ID || '',
  AUDIENCE: import.meta.env.VITE_AUTH0_AUDIENCE || '',
} as const; 
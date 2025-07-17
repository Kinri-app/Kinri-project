import { create } from 'zustand'
import { User } from '../types/apiTypes'

interface UserState {
  // User data
  user: User | null
  isAuthenticated: boolean
  
  // Loading states
  isLoadingProfile: boolean
  
  // Error states
  profileError: string | null
  
  // Actions
  setUser: (user: User | null) => void
  setAuthenticated: (isAuthenticated: boolean) => void
  setLoadingProfile: (isLoading: boolean) => void
  setProfileError: (error: string | null) => void
  clearUser: () => void
  
  // Legacy username support (for backward compatibility)
  username: string
  setUsername: (name: string) => void
}

const useUserStore = create<UserState>((set) => ({
  // Initial state
  user: null,
  isAuthenticated: false,
  isLoadingProfile: false,
  profileError: null,
  username: '',
  
  // Actions
  setUser: (user) => set({ user }),
  setAuthenticated: (isAuthenticated) => set({ isAuthenticated }),
  setLoadingProfile: (isLoadingProfile) => set({ isLoadingProfile }),
  setProfileError: (profileError) => set({ profileError }),
  clearUser: () => set({ 
    user: null, 
    isAuthenticated: false, 
    profileError: null, 
    username: '' 
  }),
  
  // Legacy username support
  setUsername: (username) => set({ username }),
}))

export default useUserStore

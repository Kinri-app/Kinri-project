import { useEffect, useCallback } from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import useUserStore from '../store/useUserStore';
import { userService } from '../services/userService';
import { User } from '../types/apiTypes';

export const useUserData = () => {
  const { isAuthenticated, getAccessTokenSilently, user: auth0User } = useAuth0();
  const {
    user,
    isLoadingProfile,
    profileError,
    setUser,
    setLoadingProfile,
    setProfileError,
    setAuthenticated,
    clearUser,
  } = useUserStore();

  // Fetch user profile from backend
  const fetchUserProfile = useCallback(async () => {
    if (!isAuthenticated) {
      clearUser();
      return;
    }

    setLoadingProfile(true);
    setProfileError(null);

    try {
      const token = await getAccessTokenSilently();
      const profileData = await userService.getProfile(token);
      
      // Merge Auth0 user data with backend profile data
      const mergedUser: User = {
        ...profileData,
        email: auth0User?.email || profileData.email,
        name: auth0User?.name || profileData.name,
        picture: auth0User?.picture || profileData.picture,
      };
      
      setUser(mergedUser);
    } catch (error: any) {
      console.error('Failed to fetch user profile:', error);
      setProfileError(error.message || 'Failed to load user profile');
    } finally {
      setLoadingProfile(false);
    }
  }, [isAuthenticated, getAccessTokenSilently, auth0User, setUser, setLoadingProfile, setProfileError, clearUser]);

  // Sync authentication state
  useEffect(() => {
    setAuthenticated(isAuthenticated);
    
    if (isAuthenticated && !user && !isLoadingProfile) {
      fetchUserProfile();
    } else if (!isAuthenticated) {
      clearUser();
    }
  }, [isAuthenticated, user, isLoadingProfile, fetchUserProfile, setAuthenticated, clearUser]);

  // Refresh user data
  const refreshUserData = useCallback(async () => {
    if (isAuthenticated) {
      await fetchUserProfile();
    }
  }, [isAuthenticated, fetchUserProfile]);

  return {
    user,
    isLoadingProfile,
    profileError,
    refreshUserData,
    isAuthenticated,
  };
}; 
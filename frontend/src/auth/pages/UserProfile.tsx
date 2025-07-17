import { useAuth0 } from "@auth0/auth0-react";
import Loader from "../../components/Loader";
import Unauthorized from "./Unauthorized.tsx";
import { useUserData } from "../../hooks/useUserData";

const UserProfile = () => {
    const { isLoading: auth0Loading } = useAuth0();
    const { user, isLoadingProfile, profileError, isAuthenticated, refreshUserData } = useUserData();

    if (auth0Loading || isLoadingProfile) return <Loader />;
    if (!isAuthenticated) return <Unauthorized />;

    return (
        <section className="bg-white grid place-content-center border-t border-gray-100">
            <div className="mx-auto w-screen max-w-screen-xl px-4 py-16 sm:px-6 sm:py-24 lg:px-8 lg:py-32">
                <div className="mx-auto max-w-xl text-center">
                    <img
                        src={user?.picture || '/default-avatar.png'}
                        alt={user?.name || 'User'}
                        className="mx-auto size-24 rounded-full shadow-md ring-2 ring-yellow-500"
                        onError={(e) => {
                            e.currentTarget.src = '/default-avatar.png';
                        }}
                    />
                    <h2 className="mt-6 text-3xl font-bold text-gray-900">{user?.name || 'Welcome!'}</h2>
                    <p className="mt-2 text-sm text-gray-500">{user?.email}</p>

                    <div className="mt-6">
                        <p className="text-base text-pretty text-gray-600 sm:text-lg/relaxed">
                            Welcome back to <span className="text-yellow-600 font-semibold">Kinri</span>, your safe
                            space for emotional insight.
                        </p>
                        
                        {profileError && (
                            <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
                                <p className="text-red-600 text-sm">
                                    Error loading profile: {profileError}
                                </p>
                                <button
                                    onClick={refreshUserData}
                                    className="mt-2 px-3 py-1 bg-red-600 text-white text-xs rounded hover:bg-red-700"
                                >
                                    Retry
                                </button>
                            </div>
                        )}
                        
                        {user && (
                            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                                <h3 className="text-lg font-semibold text-gray-900 mb-3">Profile Information</h3>
                                <div className="text-left space-y-2">
                                    <div>
                                        <span className="font-medium text-gray-700">User ID:</span>
                                        <span className="ml-2 text-gray-600">{user.id}</span>
                                    </div>
                                    <div>
                                        <span className="font-medium text-gray-700">Auth0 ID:</span>
                                        <span className="ml-2 text-gray-600 text-xs">{user.auth0_id}</span>
                                    </div>
                                    {user.created_at && (
                                        <div>
                                            <span className="font-medium text-gray-700">Member since:</span>
                                            <span className="ml-2 text-gray-600">
                                                {new Date(user.created_at).toLocaleDateString()}
                                            </span>
                                        </div>
                                    )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </section>
    );
};

export default UserProfile;

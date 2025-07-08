import {useAuth0} from "@auth0/auth0-react";
import Loader from "../../components/Loader";
import {useEffect, useState} from "react";
import axios from "axios"
import Unauthorized from "./Unauthorized.tsx";

const UserProfile = () => {
    const {isAuthenticated, getAccessTokenSilently, user, isLoading} = useAuth0();
    const [profileData, setProfileData] = useState(null);


    useEffect(() => {
        const fetchPrivateData = async () => {
            try {
                const token = await getAccessTokenSilently()
                const res = await axios.get('http://localhost:5000/api/users/profile', {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                })

                console.log({token})
                setProfileData(res.data)
            } catch (error) {
                console.error("Error fetching private data:", error)
            }
        }

        if (isAuthenticated) {
            fetchPrivateData()
        }
    }, [getAccessTokenSilently, isAuthenticated])

    if (isLoading) return <Loader/>;
    if (!isAuthenticated) return <Unauthorized/>;

    return (
        <section className="bg-white grid place-content-center border-t border-gray-100">
            <div className="mx-auto w-screen max-w-screen-xl px-4 py-16 sm:px-6 sm:py-24 lg:px-8 lg:py-32">
                <div className="mx-auto max-w-xl text-center">
                    <img
                        src={user?.picture}
                        alt={user?.name}
                        className="mx-auto size-24 rounded-full shadow-md ring-2 ring-yellow-500"
                    />
                    <h2 className="mt-6 text-3xl font-bold text-gray-900">{user?.name}</h2>
                    <p className="mt-2 text-sm text-gray-500">{user?.email}</p>

                    <div className="mt-6">
                        <p className="text-base text-pretty text-gray-600 sm:text-lg/relaxed">
                            Welcome back to <span className="text-yellow-600 font-semibold">Kinri</span>, your safe
                            space for emotional insight.
                        </p>
                        {profileData && (
                            <div className="mt-4 text-left">
                                <pre>{JSON.stringify(profileData, null, 2)}</pre>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </section>
    );
};

export default UserProfile;

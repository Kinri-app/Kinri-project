import { useAuth0 } from "@auth0/auth0-react";
import ChatBox from "../components/ChatBox.tsx";
import Loader from "../../components/Loader.tsx";
import Unauthorized from "../../auth/pages/Unauthorized.tsx";
import ErrorFallback from "../../components/ErrorFallback.tsx";

const ChatPage = () => {
    const { isAuthenticated, isLoading, error } = useAuth0();

    if (isLoading) return <Loader />
    if (!isAuthenticated) return <Unauthorized />
    if (error) return <ErrorFallback />

    return (
        <section className="container h-100% mx-auto px-4 space-y-6 py-8 max-w-4xl">
            <div className="flex flex-col md:flex-row items-start md:items-center gap-6 mb-8">
                <ChatBox />
            </div>
        </section>
    );
};

export default ChatPage;

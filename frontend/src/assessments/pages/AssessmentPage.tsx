import AssessmentQuestionnaire from "../components/AssessmentQuestionnaire.tsx";
import Loader from "../../components/Loader.tsx";
import {useAuth0} from "@auth0/auth0-react";
import Unauthorized from "../../auth/pages/Unauthorized.tsx";

function AssessmentPage() {
    const {isAuthenticated, isLoading} = useAuth0();

    if (isLoading) return <Loader/>;
    if (!isAuthenticated) return <Unauthorized/>;

    return (
        <section className="bg-white grid place-content-center border-t border-gray-100">
            <div className="mx-auto w-screen max-w-screen-xl px-4 py-16 sm:px-6 sm:py-24 lg:px-8 lg:py-32">
                <div className="mx-auto max-w-xl text-center">
                    <AssessmentQuestionnaire/>
                </div>
            </div>
        </section>
    );
}

export default AssessmentPage;
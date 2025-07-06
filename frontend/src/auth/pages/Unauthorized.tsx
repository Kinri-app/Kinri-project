import ButtonLink from "../../components/ButtonLink";
import LoginButton from "../components/LoginButton.tsx";

function Unauthorized() {
    return (
        <section className="grid place-items-center bg-white px-6 py-24 sm:py-32 lg:px-8">
            <div className="text-center">
                <p className="text-4xl font-semibold text-yellow-600">401</p>
                <h1 className="mt-4 text-5xl font-semibold tracking-tight text-balance text-gray-900 sm:text-7xl">
                    Unauthorized Access
                </h1>
                <p className="mt-6 text-lg font-medium text-pretty text-gray-500 sm:text-xl/8">
                    You must be logged in to view this page. Please log in or return to the homepage.
                </p>
                <div className="mt-6 flex justify-center gap-4">
                    <LoginButton/>
                    <ButtonLink to="/" className="border-gray-200 text-gray-700 hover:bg-gray-50 hover:text-gray-900">
                        Go back home
                    </ButtonLink>
                </div>
            </div>
        </section>
    );
}

export default Unauthorized;

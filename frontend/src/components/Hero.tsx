import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "../auth/components/LoginButton";
import ButtonLink from "./ButtonLink";

function Hero() {
    const { isAuthenticated } = useAuth0();

    return (
        <section className="bg-white grid place-content-center">
            <div className="mx-auto w-screen max-w-screen-xl px-4 py-16 sm:px-6 sm:py-24 lg:px-8 lg:py-32">
                <div className="mx-auto max-w-prose text-center">
                    <h1 className="text-4xl font-bold text-gray-900 sm:text-5xl">
                        Welcome to <span className="text-yellow-600">Kinri</span>
                    </h1>

                    <p className="mt-4 text-base text-pretty text-gray-500 sm:text-lg/relaxed">
                        Kinri is your secure space for understanding emotional experiences. Using intelligent diagnostic flows and AI-driven insight cards, we help you explore personal growth with clarity, empathy, and safety.
                    </p>

                    <div className="mt-6 flex flex-col gap-3 sm:flex-row sm:justify-center sm:gap-4">
                        {!isAuthenticated ? (
                            <LoginButton />
                        ) : (
                            <ButtonLink
                                to="/profile"
                                className="border-yellow-500 text-yellow-500 hover:border-yellow-600 hover:text-yellow-600 w-full sm:w-auto text-center"
                            >
                                Check your profile
                            </ButtonLink>
                        )}

                        <ButtonLink
                            to="/features"
                            className="border-gray-200 text-gray-700 hover:bg-gray-50 hover:text-gray-900 w-full sm:w-auto text-center"
                        >
                            Learn more
                        </ButtonLink>
                    </div>

                </div>
            </div>
        </section>

    );
}

export default Hero;

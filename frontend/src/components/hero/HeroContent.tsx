import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "../../auth/components/LoginButton";
import ButtonLink from "../ButtonLink";

const HeroContent = () => {
    const { isAuthenticated } = useAuth0();


    return (
        <div className="flex-1 p-8 md:p-12 lg:p-16">
            <div className="max-w-2xl">
                {/* Icon */}
                <div className="mb-8">
                    <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-yellow-800 to-yellow-200 rounded-2xl shadow-md">
                        <i className="fas fa-heart text-white text-2xl" />
                    </div>
                </div>

                {/* Headline */}
                <h1 className="text-4xl md:text-5xl lg:text-6xl font-light text-gray-800 mb-6 leading-tight">
                    Reflect. <span className="text-kinri-primary font-medium">Understand.</span> Heal.
                </h1>

                {/* Subtext */}
                <p className="text-lg md:text-xl text-gray-600 mb-8 leading-relaxed font-light">
                    Kinri guides you through a safe, AI-assisted emotional insight experience.
                    Take the first gentle step toward understanding yourself better.
                </p>

                {/* CTA Buttons */}
                <div className="flex flex-col sm:flex-row gap-4">
                    {!isAuthenticated ? (
                        <LoginButton />
                    ) : (
                        <ButtonLink
                            text="Start Diagnostic"
                            icon="fas fa-compass"
                            variant="primary"
                            to="/assessments"

                        />
                    )}
                    {!isAuthenticated ? (
                        <ButtonLink
                            text="Learn More"
                            icon="fas fa-info-circle"
                            variant="outline"
                            to="/learn-more"
                        />
                    ) : (
                        <ButtonLink
                            text="Chat with our AI"
                            icon="fa-solid fa-message"
                            variant="outline"
                            to="/chat"

                        />
                    )}

                </div>
            </div>
        </div>
    )
}

export default HeroContent

import ButtonLink from "./ButtonLink";

interface ErrorFallbackProps {
    error?: Error;
}

const ErrorFallback = ({ error }: ErrorFallbackProps) => {
    return (
        <div className="w-full px-4 py-16 flex justify-center items-center min-h-[60vh]">
            <div className="bg-white/80 backdrop-blur-sm rounded-3xl shadow-lg border border-gray-100/50 p-8 md:p-12 max-w-xl text-center">
                <div className="mb-6">
                    <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-yellow-800 to-yellow-200 rounded-2xl shadow-md">
                        <i className="fas fa-exclamation-triangle text-white text-2xl" />
                    </div>
                </div>

                <h2 className="text-3xl font-semibold text-gray-800 mb-4">Oops, something went wrong</h2>

                {error && <p className="text-gray-600 mb-6 text-sm">{error.message}</p>}

                <div className="flex justify-center">
                    <ButtonLink variant="outline" text="Go back home" to="/" icon="fa-solid fa-house" />
                </div>
            </div>
        </div>
    );
};

export default ErrorFallback;

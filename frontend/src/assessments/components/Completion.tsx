import { Link } from "react-router";

const Completion: React.FC = () => {

    return (
        <div className="text-center">
            <div className="mb-8">
                <i className="fas fa-check-circle text-6xl text-[#876E2C] mb-4"></i>
                <h2 className="text-3xl font-bold text-gray-800 mb-4">Assessment Complete</h2>
                <p className="text-gray-600 text-lg">
                    Thank you for taking the time to share your experiences with us.
                </p>
            </div>
            <div className="bg-[#876E2C]/10 rounded-lg p-6 mb-8">
                <p className="text-gray-700">
                    Your responses have been recorded and will help us better understand your wellness journey.
                    A summary will be available shortly.
                </p>
            </div>
            <Link to="/chat" className="bg-[#876E2C] hover:bg-[#6d5623] text-gray-100 font-semibold py-3 px-8 rounded-lg transition-colors duration-300 flex items-center justify-center mx-auto max-w-50">
                <i className="fa-solid fa-message mr-2"></i>Get an Insight
            </Link>
        </div>
    )
};

export default Completion;

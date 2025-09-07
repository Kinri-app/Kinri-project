export const ActionButtons = () => {
    return (
        <div className="flex flex-col sm:flex-row gap-4">
            <button className="flex-1 bg-[#876E2C] hover:bg-[#876E2C]/90 text-white px-6 py-3 rounded-xl font-medium transition-all duration-300 flex items-center justify-center gap-2 shadow-md hover:shadow-lg cursor-pointer">
                <i className="fas fa-play-circle"></i>
                Continue Journey
            </button>
            <button className="flex-1 bg-white hover:bg-gray-50 text-gray-700 px-6 py-3 rounded-xl font-medium transition-all duration-300 border border-gray-200 hover:border-gray-300 flex items-center justify-center gap-2 cursor-pointer">
                <i className="fas fa-chart-line"></i>
                View Progress
            </button>
            <button className="bg-purple-50 hover:bg-purple-200 text-purple-700 px-6 py-3 rounded-xl font-medium transition-all duration-300 flex items-center justify-center gap-2 cursor-pointer">
                <i className="fas fa-cog"></i>
                Settings
            </button>
        </div>
    )
}

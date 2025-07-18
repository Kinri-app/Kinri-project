interface ProgressProps {
    current: number;
    total: number;
}

const Progress: React.FC<ProgressProps> = ({ current, total }) => {
    const pct = (current / total) * 100;

    return (
        <div className="bg-white rounded-xl shadow-lg p-6 mb-8">
            <div className="flex items-center justify-between mb-4">
                <span className="text-sm font-medium text-gray-600">Progress</span>
                <span className="text-sm font-medium text-gray-600">{current} of {total}</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-3 mb-4">
                <div className="bg-[#876E2C] h-3 rounded-full transition-all duration-500 ease-out" style={{ width: `${pct}%` }} />
            </div>
            <div className="flex justify-center space-x-3">
                {Array.from({ length: total }, (_, i) => (
                    <div
                        key={i}
                        className={`w-3 h-3 rounded-full transition-all duration-300 ${i < current ? 'bg-[#876E2C]' : 'bg-gray-300'
                            }`}
                    />
                ))}
            </div>
        </div>
    );
};

export default Progress;

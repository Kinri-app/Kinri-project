interface ProgressBarProps {
    current: number;
    total: number;
}

const ProgressBar = ({current, total}: ProgressBarProps) => {
    const progress = ((current) / total) * 100;

    return (
        <div className="mt-8">
            <div className="h-3 w-full bg-gray-200 rounded-full">
                <div
                    className="h-full bg-yellow-500 rounded-full transition-all"
                    style={{width: `${progress}%`}}
                />
            </div>
            <p className="mt-2 text-sm text-gray-500 text-right">
                {Math.round(progress)}% completed
            </p>
        </div>
    );
};

export default ProgressBar;

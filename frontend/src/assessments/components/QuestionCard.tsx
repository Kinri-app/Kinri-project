import type {Answer} from "../types/assessmentTypes.ts";

interface QuestionCardProps {
    question: string;
    onAnswer: (value: Answer) => void;
}

const options: Answer[] = ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'];

const QuestionCard = ({question, onAnswer}: QuestionCardProps) => {
    return (
        <div>
            <p className="text-xl font-semibold text-gray-900 mb-4">{question}</p>
            <div className="flex flex-col md:flex-row gap-3">
                {options.map((option) => (
                    <button
                        key={option}
                        onClick={() => onAnswer(option)}
                        className="flex-1 flex justify-center rounded-md border border-gray-300 bg-white px-3 py-2 text-gray-800 hover:bg-yellow-50 hover:border-yellow-600 transition"
                    >
                        {option}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default QuestionCard;

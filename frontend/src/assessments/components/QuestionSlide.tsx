import { assessmentOptions } from "../data/questions";
import type { Question } from "../types/assessmentTypes";
import { AssessmentOption } from "./AssessmentOption";


interface QSlideProps {
    question: Question;
}

const QuestionSlide: React.FC<QSlideProps> = ({ question }) => {
    return (
        <div className="question-slide">
            <div className="mb-8">
                <h2 className="text-2xl font-semibold text-gray-800 mb-4 flex items-center">
                    <i className={`fas ${question.icon} text-[#876E2C] mr-3`}></i>
                    {question.title}
                </h2>
                <p className="text-gray-600">{question.subtitle}</p>
            </div>

            <div className="flex flex-col md:flex-row gap-3">
                {assessmentOptions.map(({ value, label }) => {
                    return (
                        <AssessmentOption
                            key={value}
                            value={value}
                            label={label}
                        />
                    );
                })}
            </div>
        </div>
    );
};

export default QuestionSlide;

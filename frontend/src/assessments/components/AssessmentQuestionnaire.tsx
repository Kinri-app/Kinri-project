import {useState} from 'react';
import {useNavigate} from 'react-router';
import QuestionCard from './QuestionCard';
import ProgressBar from './ProgressBar';
import {diagnosticQuestions} from '../utils/questions.ts';
import {type Answer, answerScores} from '../types/assessmentTypes.ts';
import {useAssessmentStore} from '../store/assessmentStore';

const AssessmentQuestionnaire = () => {
    const [current, setCurrent] = useState(0);
    const [responses, setResponses] = useState<{ id: string; score: number }[]>([]);
    const setResults = useAssessmentStore((state) => state.setResponses);
    const navigate = useNavigate();

    const handleAnswer = (answer: Answer) => {
        const currentQuestion = diagnosticQuestions[current];
        if (!currentQuestion) return;

        const score = answerScores[answer];

        // Update or insert the current response
        const updatedResponses = [
            ...responses.filter((r) => r.id !== currentQuestion.id),
            {id: currentQuestion.id, score},
        ];
        
        setResponses(updatedResponses);

        const isLast = current >= diagnosticQuestions.length - 1;

        if (isLast) {
            setResults(updatedResponses);
            navigate('/chat');
        } else {
            setCurrent((prev) => prev + 1);
        }
    };

    const currentQuestion = diagnosticQuestions[current];
    if (!currentQuestion) return null;

    return (
        <div className="max-w-xl mx-auto px-4 py-10">
            <div className="mb-6">
                <h2 className="text-lg font-medium text-gray-700">
                    Question {current + 1} of {diagnosticQuestions.length}
                </h2>
                <QuestionCard question={currentQuestion.question} onAnswer={handleAnswer}/>
            </div>

            <ProgressBar current={current} total={diagnosticQuestions.length}/>
        </div>
    );
};

export default AssessmentQuestionnaire;

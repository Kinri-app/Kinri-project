import Progress from '../components/Progress';
import QuestionSlide from '../components/QuestionSlide';
import Completion from '../components/Completion';
import { questions } from '../data/questions';
import { useAssessmentStore } from '../store/assessmentStore';
import { useEffect } from 'react';
import NotFound from '../../pages/NotFound';
import Loader from '../../components/Loader';
import Unauthorized from '../../auth/pages/Unauthorized';
import { useAuth0 } from '@auth0/auth0-react';

const AssessmentPage = () => {
    const { isAuthenticated, isLoading } = useAuth0();

    const {
        currentStep,
        currentOption,
        currentQuestion,
        answers,
        setQuestion,
        setAnswer,
        goToNext,
        goToPrev,
        resetOption,
        totalQuestions,
    } = useAssessmentStore();

    useEffect(() => {
        setQuestion(questions[currentStep])

    }, [currentStep, setQuestion, answers])

    const isCompleted = answers.length === totalQuestions;
    const isLast = answers.length === totalQuestions - 1;

    const next = () => {
        if (currentOption !== null && currentQuestion) {
            setAnswer(currentQuestion.id, currentOption)
            goToNext();
            resetOption();
        }
    };

    const back = () => {
        goToPrev();
        resetOption();
    };

    if (isLoading) return <Loader />
    if (!isAuthenticated) return <Unauthorized />
    if (!currentQuestion) return <NotFound />

    return (
        <section className="container mx-auto px-4 space-y-6 py-8 max-w-4xl">
            <header className="text-center">
                <h1 className="text-3xl font-bold text-gray-800 mb-2">Wellness Assessment</h1>
                <p className="text-gray-600">Take your time... understand your experience.</p>
            </header>

            <main className="rounded-xl shadow-lg p-8">
                {!isCompleted ? (
                    <QuestionSlide question={currentQuestion} />
                ) : (
                    <Completion />
                )}

                <footer className={`${isCompleted ? 'hidden' : 'flex justify-between items-center mt-8'}`}>
                    <button
                        onClick={back}
                        disabled={currentStep === 0}
                        className="flex items-center px-6 py-3 text-gray-600 hover:text-[#876E2C] transition-colors duration-300 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                        <i className="fas fa-arrow-left mr-2"></i>
                        Previous
                    </button>

                    <button
                        onClick={next}
                        disabled={currentOption === null}
                        className="flex items-center px-6 py-3 bg-[#876E2C] text-white rounded-lg hover:bg-[#6d5623] transition-colors duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                        {isLast ? (
                            <>
                                <i className="fas fa-check mr-2"></i> Complete
                            </>
                        ) : (
                            <>
                                Next <i className="fas fa-arrow-right ml-2"></i>
                            </>
                        )}
                    </button>
                </footer>
            </main>

            {!isCompleted && <Progress current={answers.length} total={totalQuestions} />}
        </section>
    );
};

export default AssessmentPage;

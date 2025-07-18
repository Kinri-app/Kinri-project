import { create } from "zustand";
import type { AnswerItem, Question } from "../types/assessmentTypes";
import { questions } from "../data/questions";


interface AssessmentState {
    currentOption: number | null; // Option selected
    currentQuestion: Question | null; // Current question displayed
    currentStep: number; // Current question position
    totalQuestions: number;
    answers: AnswerItem[]; // key = questionId, value = answerScore
    setAnswer: (questionId: string, answerScore: number) => void;
    setQuestion: (question: Question) => void;
    setOption: (optionSelected: number) => void;
    goToNext: () => void;
    goToPrev: () => void;
    reset: () => void;
    resetOption: () => void;
    resetAnswers: () => void;
}

export const useAssessmentStore = create<AssessmentState>((set, get) => ({
    currentStep: 0,
    currentOption: null,
    currentQuestion: null,
    totalQuestions: questions.length,
    answers: [],
    setQuestion: (newCurrentQuestion) =>
        set(() => ({
            currentQuestion: newCurrentQuestion,
        })),

    setOption: (optionSelected) =>
        set(() => ({
            currentOption: optionSelected,
        })),

    setAnswer: (questionId, answerScore) =>
        set((state) => ({
            answers: [...state.answers, { id: questionId, score: answerScore }],
        })),

    goToNext: () => {
        const nextStep = get().currentStep + 1;
        if (nextStep < get().totalQuestions) {
            set({ currentStep: nextStep });
        }
    },

    goToPrev: () => {
        const { currentStep, answers } = get();
        const prevStep = currentStep - 1;
        if (prevStep >= 0) {
            set({ currentStep: prevStep, answers: answers.slice(0, -1) });
        }
    },

    reset: () =>
        set(() => ({
            currentStep: 0,
            currentOption: null,
            answers: [],
        })),

    resetOption: () => set({ currentOption: null }),
    resetAnswers: () => set({ answers: [] }),
}));

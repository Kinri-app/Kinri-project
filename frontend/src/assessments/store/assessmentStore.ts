import {create} from 'zustand'

interface ResponseItem {
    id: string;
    score: number;
}

interface AssessmentResults {
    responses: ResponseItem[] | null;
    setResponses: (newResults: ResponseItem[]) => void;
    clearResponses: () => void;
}

export const useAssessmentStore = create<AssessmentResults>((set) => ({
    responses: null,
    setResponses: (newResponses) => set({responses: newResponses}),
    clearResponses: () => set({responses: null}),
}));

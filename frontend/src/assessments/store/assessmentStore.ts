import {create} from 'zustand'
import type {AssessmentResponseItem} from "../types/assessmentTypes.ts";


interface AssessmentResults {
    responses: AssessmentResponseItem[] | null;
    setResponses: (newResults: AssessmentResponseItem[]) => void;
    clearResponses: () => void;
}

export const useAssessmentStore = create<AssessmentResults>((set) => ({
    responses: null,
    setResponses: (newResponses) => set({responses: newResponses}),
    clearResponses: () => set({responses: null}),
}));

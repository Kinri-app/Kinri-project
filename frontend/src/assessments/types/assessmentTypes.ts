export type Answer = 'Never' | 'Rarely' | 'Sometimes' | 'Often' | 'Always';

export const answerScores: Record<Answer, number> = {
    Never: 0,
    Rarely: 1,
    Sometimes: 2,
    Often: 3,
    Always: 4,
};

export interface ConditionWeights {
    [condition: string]: number;
}

export interface DiagnosticQuestion {
    id: string;
    question: string;
    conditions: ConditionWeights;
}

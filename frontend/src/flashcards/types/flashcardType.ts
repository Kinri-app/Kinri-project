export interface Flashcard {
    id: number;
    question: string;
    answer: string;
    card_id: string;
    condition: string[];
    emotion: string[];
    narrative_type: string[];
    usage_mode: string[];
}

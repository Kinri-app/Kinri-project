import type { Flashcard } from "../types/flashcardTypes.ts";

interface FlashcardItemProps {
    flashcard: Flashcard;
}

const FlashcardItem = ({ flashcard }: FlashcardItemProps) => (
    <div className="p-4 border rounded-lg shadow-sm bg-white">
        <h3 className="font-semibold text-gray-900">{flashcard.question}</h3>
        <p className="mt-2 text-gray-700 text-sm whitespace-pre-wrap">
            {flashcard.answer}
        </p>
    </div>
);

export default FlashcardItem;

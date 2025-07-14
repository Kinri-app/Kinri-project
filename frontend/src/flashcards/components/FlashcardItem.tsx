import type { Flashcard } from "../types/flashcardTypes.ts";

interface FlashcardItemProps {
    flashcard: Flashcard;
}

const FlashcardItem = ({ flashcard }: FlashcardItemProps) => (
    <div className="p-6 border rounded-lg shadow-sm bg-white hover:shadow-md transition-shadow">
        <h3 className="font-semibold text-gray-900 text-lg mb-3">{flashcard.question}</h3>
        <p className="text-gray-700 text-sm whitespace-pre-wrap leading-relaxed mb-3">
            {flashcard.answer}
        </p>
        {flashcard.tags && flashcard.tags.length > 0 && (
            <div className="flex flex-wrap gap-2">
                {flashcard.tags.map((tag, index) => (
                    <span 
                        key={index} 
                        className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full"
                    >
                        {tag}
                    </span>
                ))}
            </div>
        )}
    </div>
);

export default FlashcardItem;

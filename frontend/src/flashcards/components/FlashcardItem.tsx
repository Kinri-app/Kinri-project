import { useState } from 'react';
import type { Flashcard } from '../types/flashcardType';

interface Props {
    card: Flashcard;
}

export const FlashcardItem = ({ card }: Props) => {
    const [flipped, setFlipped] = useState(false);

    return (
        <article
            onClick={() => setFlipped(!flipped)}
            className="h-48 perspective cursor-pointer"
        >
            <div className={`relative w-full h-full duration-700 preserve-3d ${flipped ? 'rotate-y-180' : ''}`}>
                {/* Front */}
                <div className="absolute w-full h-full backface-hidden text-white p-4 flex items-center justify-center shadow-lg rounded-xl">
                    <div className="text-center">
                        <i className={`${card.icon} text-kinri-primary text-2xl mb-3`}></i>
                        <h4 className="font-semibold text-gray-800">{card.question}</h4>
                    </div>
                </div>

                {/* Back */}
                <div className="absolute w-full h-full backface-hidden rotate-y-180 bg-gradient-to-br from-yellow-50/50 via-white to-yellow-50/50 text-gray-800 p-4 flex items-center justify-center shadow-lg rounded-xl">
                    <p className="text-sm text-center">{card.answer}</p>
                </div>
            </div>
        </article>

    );
};

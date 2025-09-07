import Loader from "../../components/Loader.tsx";
import { useFlashcardStore } from "../store/flashcardStore.ts";
import { FlashcardItem } from "./FlashcardItem.tsx";
import ErrorFallback from "../../components/ErrorFallback.tsx";
import { useEffect } from "react";

const FlashcardGrid = () => {
    const { flashcards, loadFlashcards, loading, error } = useFlashcardStore();

    useEffect(() => {
        loadFlashcards();
    }, [loadFlashcards]);
    // TODO: Make http request

    if (loading) return <Loader />;
    if (error) return <ErrorFallback />;

    return (
        <section id="flashcard-grid" className="space-y-6">
            <h2 className="text-3xl font-bold text-gray-800 text-center">Reflection Cards</h2>
            <p className="text-gray-600 text-center max-w-2xl mx-auto">
                Explore different aspects of your emotional well-being
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {flashcards.map((card, i) => (
                    <FlashcardItem key={i} card={card} />
                ))}
            </div>
        </section>
    );
};

export default FlashcardGrid;
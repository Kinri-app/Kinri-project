import { useEffect } from "react";
import Loader from "../../components/Loader.tsx";
import { useFlashcardStore } from "../store/flashcardStore.ts";
import FlashcardItem from "./FlashcardItem.tsx";

const FlashcardList = () => {
    const { flashcards, loadFlashcards, loading, error } = useFlashcardStore();

    useEffect(() => {
        loadFlashcards();
    }, [loadFlashcards]);

    if (loading) return <Loader />;
    if (error) return <p className="text-red-500">{error}</p>;

    return (
        <div className="space-y-4">
            {flashcards.map((card, idx) => (
                <FlashcardItem key={idx} flashcard={card} />
            ))}
        </div>
    );
};

export default FlashcardList;

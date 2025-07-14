import FlashcardList from "../components/FlashcardList.tsx";

const FlashcardPage = () => (
    <section className="bg-white grid place-content-center border-t border-gray-100">
        <div className="mx-auto w-screen max-w-screen-xl px-4 py-16">
            <div className="mx-auto max-w-xl">
                <FlashcardList />
            </div>
        </div>
    </section>
);

export default FlashcardPage;

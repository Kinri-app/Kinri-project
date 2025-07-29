export interface Flashcard {
    icon: string;
    question: string;
    answer: string;
}

export const dummyFlashcards: Flashcard[] = [
    {
        icon: "fas fa-brain",
        question: "What thoughts are occupying your mind?",
        answer: "Notice your thoughts without getting caught up in them. They are temporary visitors in your mind.",
    },
    {
        icon: "fas fa-leaf",
        question: "How is your body feeling right now?",
        answer: "Your body holds wisdom. Listen to what it's telling you about your current state.",
    },
    {
        icon: "fas fa-users",
        question: "How are your relationships affecting you?",
        answer: "Relationships shape our emotional landscape. Reflect on the connections that matter most.",
    },
    {
        icon: "fas fa-star",
        question: "What brought you joy today?",
        answer: "Celebrating small moments of joy helps build resilience and positive perspective.",
    },
    {
        icon: "fas fa-mountain",
        question: "What challenges are you facing?",
        answer: "Challenges are opportunities for growth. You have the strength to navigate them.",
    },
    {
        icon: "fas fa-heart",
        question: "How can you show yourself compassion?",
        answer: "Self-compassion is the foundation of emotional well-being. Treat yourself with kindness.",
    },
];

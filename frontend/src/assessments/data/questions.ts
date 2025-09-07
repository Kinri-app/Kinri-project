// File: data/questions.ts

import type { Option, Question } from "../types/assessmentTypes";

export const questions: Question[] = [
    {
        id: "q1",
        icon: "fas fa-shield-alt",
        title: "Do you ever feel like your body is bracing for impact?",
        subtitle: "Even in safe situations, do you feel on edge?",
    },
    {
        id: "q2",
        icon: "fas fa-comment-slash",
        title: "Do you find it hard to explain how you're feeling?",
        subtitle: "Even to people close to you?",
    },
    {
        id: "q3",
        icon: "fas fa-ban",
        title: "Do you avoid things just because they’re uncomfortable?",
        subtitle: "Even when they're not actually dangerous?",
    },
    {
        id: "q4",
        icon: "fas fa-brain",
        title: "Does your brain go blank in high-pressure situations?",
        subtitle: "Even when you're well prepared?",
    },
    {
        id: "q5",
        icon: "fas fa-mask",
        title: "Do you feel like you're performing a version of yourself?",
        subtitle: "Acting as others expect rather than being yourself?",
    },
    {
        id: "q6",
        icon: "fas fa-tools",
        title: "Do you feel like you're constantly adapting to survive?",
        subtitle: "Rather than adapting to thrive?",
    },
    {
        id: "q7",
        icon: "fas fa-moon",
        title: "Are your thoughts too loud to fall asleep?",
        subtitle: "Even when you're physically exhausted?",
    },
    {
        id: "q8",
        icon: "fas fa-thumbs-up",
        title: "Do you say 'yes' to avoid discomfort?",
        subtitle: "Even when you don't really want to?",
    },
    {
        id: "q9",
        icon: "fas fa-exclamation-triangle",
        title: "Do you feel unsafe, even in safe places?",
        subtitle: "A constant feeling of being at risk?",
    },
    {
        id: "q10",
        icon: "fas fa-question-circle",
        title: "Do you frequently seek reassurance from others?",
        subtitle: "Even after they've already given you an answer?",
    },
];

export const assessmentOptions: Option[] = [
    {
        value: 0,
        label: "Never",
    },
    {
        value: 1,
        label: "Rarely",
    },
    {
        value: 2,
        label: "Sometimes",
    },
    {
        value: 3,
        label: "Often",
    },
    {
        value: 4,
        label: "Always",
    },
];

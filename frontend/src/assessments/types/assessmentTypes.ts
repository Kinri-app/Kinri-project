export type Answer = "Never" | "Rarely" | "Sometimes" | "Often" | "Always";


export interface Option {
    value: number;
    label: string;
}

export interface Question {
    id: string;
    icon: string; // FontAwesome class
    title: string;
    subtitle: string;
}

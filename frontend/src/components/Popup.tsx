import { useEffect } from "react";
import clsx from "clsx";

type PopupType = "notification" | "error" | "warning";

interface PopupProps {
    type: PopupType;
    title: string;
    message: string;
    actionText: string;
    onClose: () => void;
    onAction?: () => void;
    isOpen: boolean;
}

const typeStyles = {
    notification: {
        icon: "fas fa-info",
        iconBg: "bg-blue-100 text-blue-600",
        actionBtn: "bg-blue-500 hover:bg-blue-600 text-white",
    },
    error: {
        icon: "fas fa-exclamation-triangle",
        iconBg: "bg-red-100 text-red-600",
        actionBtn: "bg-red-500 hover:bg-red-600 text-white",
    },
    warning: {
        icon: "fas fa-exclamation-circle",
        iconBg: "bg-orange-100 text-orange-600",
        actionBtn: "bg-orange-500 hover:bg-orange-600 text-white",
    },
};

export const Popup = ({
    type,
    title,
    message,
    actionText,
    onClose,
    onAction,
    isOpen,
}: PopupProps) => {
    const { icon, iconBg, actionBtn } = typeStyles[type];

    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === "Escape") onClose();
        };
        if (isOpen) {
            document.body.style.overflow = "hidden";
            document.addEventListener("keydown", handleKeyDown);
        } else {
            document.body.style.overflow = "auto";
        }
        return () => {
            document.body.style.overflow = "auto";
            document.removeEventListener("keydown", handleKeyDown);
        };
    }, [isOpen, onClose]);

    if (!isOpen) return null;

    return (
        <div
            className="fixed inset-0 bg-black/20 bg-opacity-50 z-50 flex items-center justify-center"
            onClick={(e) => {
                if (e.target === e.currentTarget) onClose();
            }}
        >
            <div className="relative bg-white rounded-2xl shadow-2xl max-w-md w-full mx-4 overflow-hidden">
                {/* Close Button */}
                <button
                    onClick={onClose}
                    className="absolute top-4 right-4 w-8 h-8 bg-gray-100 hover:bg-gray-200 rounded-full flex items-center justify-center text-gray-500 hover:text-gray-700 transition-all duration-200 z-10"
                >
                    <span className="text-lg font-medium">×</span>
                </button>

                {/* Header */}
                <div className="px-6 pt-6 pb-4 border-b border-gray-100">
                    <div className="flex items-center space-x-3">
                        <div className={clsx("w-10 h-10 rounded-full flex items-center justify-center", iconBg)}>
                            <i className={clsx(icon, "text-sm")}></i>
                        </div>
                        <h3 className="text-xl font-semibold text-gray-800">{title}</h3>
                    </div>
                </div>

                {/* Body */}
                <div className="px-6 py-6">
                    <p className="text-gray-600 leading-relaxed">{message}</p>
                </div>

                {/* Footer */}
                <div className="px-6 pb-6">
                    <div className="flex justify-end space-x-3">
                        <button
                            onClick={onClose}
                            className="px-4 py-2 text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200"
                        >
                            Cancel
                        </button>
                        <button
                            onClick={onAction || onClose}
                            className={clsx("px-6 py-2 rounded-lg font-medium transition-all duration-200 shadow-sm", actionBtn)}
                        >
                            {actionText}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

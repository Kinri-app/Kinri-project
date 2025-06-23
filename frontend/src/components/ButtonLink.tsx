import React from "react";
import { Link } from "react-router";

interface ButtonLinkProps {
    to: string;
    children: React.ReactNode;
    className?: string;
    onClick?: () => void;
}

const ButtonLink: React.FC<ButtonLinkProps> = ({
    to,
    children,
    className = "",
    onClick,
}) => {
    return (
        <Link
            to={to}
            onClick={onClick}
            className={`inline-block rounded border px-6 py-3 font-medium shadow-sm transition-colors ${className}`}
        >
            {children}
        </Link>
    );
};

export default ButtonLink;

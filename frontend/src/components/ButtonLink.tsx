import { Link } from "react-router";

interface ButtonLinkProps {
    to: string;
    text: string
    icon?: string
    variant?: 'primary' | 'outline'
    fontSize?: string
    handleClick?: () => void
}

const ButtonLink = ({
    to,
    variant = 'primary',
    fontSize = "text-lg",
    text,
    icon,
    handleClick,
}: ButtonLinkProps) => {
    const base = 'px-8 py-4 rounded-2xl font-medium transition-all duration-300 flex items-center justify-center gap-3'
    const variants = {
        primary: 'bg-[#876E2C] hover:bg-[#876E2C]/90 text-white shadow-lg hover:shadow-xl transform',
        outline: 'bg-white/70 hover:bg-white text-kinri-primary border border-yellow-800/20 hover:border-yellow-800/40',
    }

    return (
        <Link
            to={to}
            onClick={handleClick}
            className={`${base} ${variants[variant]} group ${fontSize} cursor-pointer`}
        >
            {icon && <i className={`${icon} text-xl group-hover:rotate-12 transition-transform duration-300`} />}
            {text}
        </Link>
    );
};

export default ButtonLink;

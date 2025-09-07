import { Link } from "react-router";

const navLinks = [
    { label: "Home", to: "/" },
    { label: "Flashcards", to: "/flashcards" },

];

interface NavLinksProps {
    className: string;
}

const NavLinks = ({ className }: NavLinksProps) => (
    <>
        {navLinks.map((link) => (
            <Link to={link.to} key={link.label} className={className}>
                {link.label}
            </Link>
        ))}
    </>
);

export default NavLinks;

import { useAuth0 } from "@auth0/auth0-react";

interface LoginButtonProps {
    className?: string
}

const defaultClassName = "rounded-md bg-yellow-600 px-5 py-2.5 text-sm font-medium text-white shadow-sm hover:bg-yellow-700 transition cursor-pointer"

const LoginButton = ({ className }: LoginButtonProps) => {
    const { loginWithRedirect } = useAuth0();

    return (
        <button
            onClick={() => loginWithRedirect()}
            className={className ?? defaultClassName}
        >
            Login
        </button>
    );
};

export default LoginButton;

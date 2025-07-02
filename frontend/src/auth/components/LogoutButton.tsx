import { useAuth0 } from "@auth0/auth0-react";

interface LogoutButtonProps {
    className?: string;
}

const defaultClassName =
    "rounded-md px-5 py-2.5 text-sm font-medium text-red-700 cursor-pointer";

const LogoutButton = ({ className }: LogoutButtonProps) => {
    const { logout } = useAuth0();

    return (
        <button
            onClick={() =>
                logout({
                    logoutParams: { returnTo: window.location.origin },
                })
            }
            className={className ?? defaultClassName}
        >
            Logout
        </button>
    );
};

export default LogoutButton;

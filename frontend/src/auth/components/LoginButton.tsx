import { useAuth0 } from "@auth0/auth0-react";
import Button from "../../components/Button";

interface LoginButtonProps {
    text?: string
}


const LoginButton = ({ text }: LoginButtonProps) => {
    const { loginWithRedirect } = useAuth0();

    return (
        <Button
            text={
                text ?? "Log in to your account"
            }
            icon="fas fa-sign-in-alt"
            variant="primary"
            handleClick={() => loginWithRedirect()}
        />
    );
};

export default LoginButton;

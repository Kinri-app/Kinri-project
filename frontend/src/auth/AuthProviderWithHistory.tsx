import {Auth0Provider, type AppState} from "@auth0/auth0-react"
import type {ReactNode} from "react"
import {useNavigate} from "react-router"

interface Props {
    children: ReactNode
}

const domain = import.meta.env.VITE_AUTH0_DOMAIN
const clientId = import.meta.env.VITE_AUTH0_CLIENT_ID
const audience = import.meta.env.VITE_AUTH0_AUDIENCE

export default function AuthProviderWithHistory({children}: Props) {
    const navigate = useNavigate()


    const onRedirectCallback = (appState: AppState | undefined) => {
        navigate(appState?.returnTo || window.location.pathname)
    }

    return (
        <Auth0Provider
            domain={domain}
            clientId={clientId}
            authorizationParams={{
                redirect_uri: window.location.origin,
                audience
            }}
            onRedirectCallback={onRedirectCallback}
        >
            {children}
        </Auth0Provider>
    )
}

import {Auth0Provider, type AppState} from "@auth0/auth0-react"
import type {ReactNode} from "react"
import {useNavigate} from "react-router"
import { AUTH0_CONFIG } from "../config/api"

interface Props {
    children: ReactNode
}

const domain = AUTH0_CONFIG.DOMAIN
const clientId = AUTH0_CONFIG.CLIENT_ID
const audience = AUTH0_CONFIG.AUDIENCE

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

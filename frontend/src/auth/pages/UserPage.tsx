import { useAuth0 } from "@auth0/auth0-react"
import { ActionButtons } from "../components/ActionButtons"
import { Avatar } from "../components/Avatar"
import { InsightCard } from "../components/InsightCard"
import { UserInfo } from "../components/UserInfo"
import Unauthorized from "./Unauthorized"
import Loader from "../../components/Loader"

export const UserPage = () => {
    const { user, isAuthenticated, isLoading } = useAuth0();

    if (isLoading) return <Loader />
    if (!isAuthenticated || !user) return <Unauthorized />

    return (
        <section className="container h-100% mx-auto px-4 space-y-6 py-8 max-w-4xl">
            <div className="flex flex-col md:flex-row items-start md:items-center gap-6 mb-8">
                <Avatar picture={user?.picture} />
                <UserInfo givenName={user?.given_name} familyName={user.family_name} email={user.email} />
            </div>
            <InsightCard />
            <ActionButtons />
        </section>
    )
}

import { useState } from "react";
import { Bars3Icon } from "@heroicons/react/24/outline";
import NavLogo from "./NavLogo";
import MobileMenu from "./MobileMenu";
import LoginButton from "../auth/components/LoginButton";
import NavLinks from "./NavLinks";
import { useAuth0 } from "@auth0/auth0-react";
import LogoutButton from "../auth/components/LogoutButton";

const HeaderNav = () => {
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
    const { isAuthenticated } = useAuth0();

    return (
        <header className="bg-white sticky top-0">
            <nav className="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global">
                <div className="flex lg:flex-1">
                    <NavLogo />
                </div>
                <div className="flex lg:hidden">
                    <button onClick={() => setMobileMenuOpen(true)} className="p-2 text-gray-700 cursor-pointer">
                        <Bars3Icon className="h-7 w-7" />
                    </button>
                </div>
                <div className="hidden lg:flex lg:gap-x-12">
                    <NavLinks className={"text-sm font-semibold text-gray-900"} />
                </div>
                <div className="hidden lg:flex lg:flex-1 lg:justify-end cursor-pointer">
                    {
                        isAuthenticated ?
                            <LogoutButton />
                            :
                            <LoginButton />
                    }
                </div>
            </nav>
            <MobileMenu open={mobileMenuOpen} setOpen={setMobileMenuOpen} />
        </header>
    );
};

export default HeaderNav;


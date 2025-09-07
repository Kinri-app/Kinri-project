import { useState } from "react";
import NavLogo from "./NavLogo";
import MobileMenu from "./MobileMenu";
import NavLinks from "./NavLinks";
import { useAuth0 } from "@auth0/auth0-react";
import GenericPopover, { type PopoverItem } from "./GenericPopover";
import Button from "./Button"

const HeaderNav = () => {
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
    const { isAuthenticated, user, logout, loginWithRedirect } = useAuth0();

    const accountMenuItems: PopoverItem[] = [
        {
            label: "My profile",
            to: "/profile",
        },
        {
            label: "Logout",
            onClick: () =>
                logout({
                    logoutParams: {
                        returnTo: window.location.origin,
                    },
                }),
            className: "text-red-700"
        },
    ];

    return (
        <header className="bg-gradient-to-br from-yellow-50 via-white to-yellow-50 sticky top-0 shadow-sm z-50">
            <nav className="mx-auto flex max-w-7xl items-center justify-between p-4 lg:px-8" aria-label="Global">
                <div className="flex lg:flex-1">
                    <NavLogo />
                </div>
                <div className="flex lg:hidden">
                    <button onClick={() => setMobileMenuOpen(true)} className="p-2 text-gray-900 hover:text-[#876E2C] duration-300 cursor-pointer">
                        <i className="fas fa-bars text-xl"></i>
                    </button>
                </div>
                <div className="hidden lg:flex lg:gap-x-12">
                    <NavLinks className={"text-sm font-semibold text-gray-900 hover:text-[#876E2C] duration-300"} />
                </div>
                <div className="hidden lg:flex lg:flex-1 lg:justify-end cursor-pointer">
                    {
                        isAuthenticated ?
                            <GenericPopover label={user?.name ?? "Account"} items={accountMenuItems} />
                            :
                            <Button
                                text="Login"
                                icon="fas fa-sign-in-alt"
                                fontSize="text-sm"
                                handleClick={() => loginWithRedirect()}
                            />
                    }
                </div>
            </nav>
            <MobileMenu open={mobileMenuOpen} setOpen={setMobileMenuOpen} />
        </header>
    );
};

export default HeaderNav;


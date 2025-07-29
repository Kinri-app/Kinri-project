import {
    Dialog,
    DialogPanel,
} from "@headlessui/react";
import NavLinks from "./NavLinks";
import { useAuth0 } from "@auth0/auth0-react";
import type { PopoverItem } from "./GenericPopover";
import MobileDisclosure from "./MobileDisclosure";
import Button from "./Button";

interface MobileMenuProps {
    open: boolean;
    setOpen: (open: boolean) => void;
}

const MobileMenu = ({
    open,
    setOpen,
}: MobileMenuProps) => {

    const { isAuthenticated, logout, user, loginWithRedirect } = useAuth0();

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
            className: "text-red-700 hover:text-red-800"
        },
    ];

    return (
        <Dialog open={open} onClose={setOpen} className="lg:hidden">
            <DialogPanel className="fixed inset-y-0 right-0 z-50 w-full shadow-sm bg-white p-6 sm:max-w-sm">
                <button className="flex p-2 ml-auto text-gray-900 hover:text-[#876E2C] duration-300 cursor-pointer" onClick={() => setOpen(false)}>
                    <i className="fa-solid fa-x"></i>
                </button>
                <div className="mt-6 space-y-4">
                    <NavLinks className="block text-base font-semibold text-gray-900 hover:text-[#876E2C] duration-300 rounded px-3 py-2" />
                    {
                        isAuthenticated ?
                            <MobileDisclosure label={user?.name ?? "Account"} items={accountMenuItems} /> :
                            <Button
                                text="Login"
                                icon="fas fa-sign-in-alt"
                                fontSize="text-sm"
                                handleClick={() => loginWithRedirect()}
                            />
                    }

                </div>
            </DialogPanel>
        </Dialog>
    );
};

export default MobileMenu;

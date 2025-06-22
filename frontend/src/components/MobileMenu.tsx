import {
    Dialog,
    DialogPanel,
} from "@headlessui/react";
import { XMarkIcon } from "@heroicons/react/20/solid";
import NavLinks from "./NavLinks";
import LoginButton from "../auth/components/LoginButton";
import { useAuth0 } from "@auth0/auth0-react";
import type { PopoverItem } from "./GenericPopover";
import MobileDisclosure from "./MobileDisclosure";

interface MobileMenuProps {
    open: boolean;
    setOpen: (open: boolean) => void;
}

const MobileMenu = ({
    open,
    setOpen,
}: MobileMenuProps) => {

    const { isAuthenticated, logout, user } = useAuth0();

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
        <Dialog open={open} onClose={setOpen} className="lg:hidden">
            <DialogPanel className="fixed inset-y-0 right-0 z-50 w-full shadow-sm bg-white p-6 sm:max-w-sm">
                <button className="flex p-2 ml-auto" onClick={() => setOpen(false)}>
                    <XMarkIcon className="h-7 w-7 text-gray-700 cursor-pointer" />
                </button>
                <div className="mt-6 space-y-4">
                    <NavLinks className="block text-base font-semibold text-gray-900 hover:bg-gray-100 rounded px-3 py-2" />
                    {
                        isAuthenticated ?
                            <MobileDisclosure label={user?.name ?? "Account"} items={accountMenuItems} /> :
                            <LoginButton className="block w-full text-left text-base font-semibold hover:bg-gray-50 rounded px-3 py-2 text-yellow-600 cursor-pointer" />
                    }

                </div>
            </DialogPanel>
        </Dialog>
    );
};

export default MobileMenu;

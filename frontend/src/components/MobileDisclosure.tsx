import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
} from "@headlessui/react";
import { ChevronDownIcon } from "@heroicons/react/20/solid";
import { Link } from "react-router";

export interface DisclosureItem {
    label: string;
    to?: string;
    onClick?: () => void;
    className?: string;
}

interface MobileDisclosureProps {
    label: string;
    items: DisclosureItem[];
}

const baseItemClass =
    "block w-full text-left cursor-pointer rounded-lg py-2 pr-3 pl-6 text-sm font-semibold hover:bg-gray-50 transition";

const MobileDisclosure = ({ label, items }: MobileDisclosureProps) => {
    return (
        <Disclosure as="div" className="">
            <DisclosureButton className="group flex w-full items-center justify-between rounded-sm py-2 pr-3.5 pl-3 text-base font-semibold text-gray-900 hover:bg-gray-100 cursor-pointer">
                {label}
                <ChevronDownIcon
                    aria-hidden="true"
                    className="size-5 flex-none group-data-open:rotate-180 transition"
                />
            </DisclosureButton>

            <DisclosurePanel className="mt-2 space-y-1">
                {items.map((item) =>
                    item.to ? (
                        <Link
                            key={item.label}
                            to={item.to}
                            className={`${baseItemClass} ${item.className || "text-gray-900"}`}
                        >
                            {item.label}
                        </Link>
                    ) : (
                        <button
                            key={item.label}
                            onClick={item.onClick}
                            className={`${baseItemClass} ${item.className || "text-gray-900"}`}
                        >
                            {item.label}
                        </button>
                    )
                )}
            </DisclosurePanel>
        </Disclosure>
    );
};

export default MobileDisclosure;

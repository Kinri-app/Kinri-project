import { Popover, PopoverButton, PopoverPanel } from '@headlessui/react'
import { Link } from 'react-router'


export interface PopoverItem {
    label: string
    to?: string
    className?: string
    onClick?: () => void
}

interface GenericPopoverProps {
    label: string
    items: PopoverItem[]
}

const popoverItemClass = "block w-full text-left text-sm font-semibold text-gray-900 px-3 py-2 cursor-pointer"

const GenericPopover = ({ label, items }: GenericPopoverProps) => {
    return (
        <Popover className="relative">
            <PopoverButton
                className="flex items-center gap-1 text-sm font-medium outline-0 text-gray-900 hover:text-[#876E2C] duration-300  cursor-pointer">
                {label}

                <i className="fas fa-chevron-down ml-1 text-xs" aria-hidden="true"></i>
            </PopoverButton>

            <PopoverPanel
                className="absolute right-0 z-10 mt-2 w-64 rounded-md bg-white shadow-lg ring-1 ring-gray-900/10 overflow-hidden">
                {items.map((item, index) => (
                    item.to ? (
                        <Link
                            key={index}
                            to={item.to}
                            className={`${popoverItemClass} ${item.className || "text-gray-900 hover:text-[#876E2C] duration-300"}`}
                        >
                            {item.label}
                        </Link>
                    ) : (
                        <button
                            key={index}
                            onClick={item.onClick}
                            className={`${popoverItemClass} ${item.className || "text-gray-900 hover:text-[#876E2C] duration-300"}`}
                        >
                            {item.label}
                        </button>
                    )
                ))}
            </PopoverPanel>
        </Popover>
    )
}

export default GenericPopover

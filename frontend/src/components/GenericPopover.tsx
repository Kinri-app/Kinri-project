import {Popover, PopoverButton, PopoverPanel} from '@headlessui/react'
import {ChevronDownIcon} from '@heroicons/react/24/outline'
import {Link} from 'react-router'


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

const popoverItemClass = "block w-full text-left text-sm font-semibold text-gray-900 hover:bg-gray-100 px-3 py-2 cursor-pointer"

const GenericPopover = ({label, items}: GenericPopoverProps) => {
    return (
        <Popover className="relative">
            <PopoverButton
                className="flex items-center gap-1 text-sm font-medium text-gray-900 hover:underline outline-0 cursor-pointer">
                {label}
                <ChevronDownIcon className="w-4 h-4 text-gray-900" aria-hidden="true"/>
            </PopoverButton>

            <PopoverPanel
                className="absolute right-0 z-10 mt-2 w-64 rounded-md bg-white shadow-lg ring-1 ring-gray-900/10 overflow-hidden">
                {items.map((item, index) => (
                    item.to ? (
                        <Link
                            key={index}
                            to={item.to}
                            className={`${popoverItemClass} ${item.className}`}
                        >
                            {item.label}
                        </Link>
                    ) : (
                        <button
                            key={index}
                            onClick={item.onClick}
                            className={`${popoverItemClass} ${item.className}`}
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

type ButtonProps = {
    text: string
    icon?: string
    variant?: 'primary' | 'outline'
    fontSize?: string
    isDisabled?: boolean
    handleClick: () => void
}

const Button = ({ text, icon, isDisabled, variant = 'primary', fontSize = "text-lg", handleClick }: ButtonProps) => {
    const base = 'px-8 py-4 rounded-2xl font-medium transition-all duration-300 flex items-center justify-center gap-3'
    const variants = {
        primary: 'bg-[#876E2C] hover:bg-[#876E2C]/90 text-white shadow-lg hover:shadow-xl transform',
        outline: 'bg-white/70 hover:bg-white text-kinri-primary border border-yellow-800/20 hover:border-yellow-800/40',
    }

    return (
        <button disabled={isDisabled} className={`${base} ${variants[variant]} group ${fontSize} cursor-pointer`} onClick={handleClick}>
            {icon && <i className={`${icon} text-xl group-hover:rotate-12 transition-transform duration-300`} />}
            {text}
        </button>
    )
}

export default Button

const HeroVisual = () => {
    return (
        <div className="flex-1 p-8 md:p-12 lg:p-16 flex items-center justify-center">
            <div className="relative">
                {/* Main Circle */}
                <div className="w-64 h-64 md:w-80 md:h-80 rounded-full bg-gradient-to-br from-yellow-50/50 via-white to-yellow-50/50 flex items-center justify-center shadow-2xl">
                        <i className="fas fa-seedling text-6xl md:text-7xl text-kinri-primary" />
                </div>

                {/* Floating Elements */}
                <div className="absolute -top-4 -right-4 w-12 h-12 rounded-full flex items-center justify-center">
                    <i className="fas fa-star text-kinri-primary" />
                </div>
                <div className="absolute -bottom-6 -left-6 w-16 h-16  bg-gradient-to-br from-yellow-50/50 via-white to-yellow-50/50 rounded-full flex items-center justify-center">
                    <i className="fas fa-leaf text-kinri-primary text-xl" />
                </div>
            </div>
        </div>
    )
}

export default HeroVisual

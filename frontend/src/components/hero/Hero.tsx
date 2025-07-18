import HeroContent from "./HeroContent"
import HeroVisual from "./HeroVisual"

const Hero = () => {
    return (
        <section className="grid place-content-center">
            <div className="flex flex-col lg:flex-row items-center">
                <HeroContent />
                <HeroVisual />
            </div>
        </section>
    )
}

export default Hero

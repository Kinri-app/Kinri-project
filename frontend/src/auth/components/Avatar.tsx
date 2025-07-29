type AvatarProps = {
    picture?: string;
};

export const Avatar = ({ picture }: AvatarProps) => {
    return (
        <div className="relative">
            <div className="w-20 h-20 md:w-24 md:h-24 rounded-2xl flex items-center justify-center shadow-lg overflow-hidden bg-kinri-primary">
                {picture ? (
                    <img
                        src={picture}
                        alt="User Avatar"
                        className="w-full h-full object-cover"
                    />
                ) : (
                    <i className="fas fa-user text-white text-2xl md:text-3xl" aria-hidden="true"></i>
                )}
            </div>
            <div className="absolute -bottom-1 -right-1 w-6 h-6 bg-green-400 rounded-full border-[3px] border-white flex items-center justify-center">
                <i className="fas fa-check text-white text-xs"></i>
            </div>
        </div>
    );
};

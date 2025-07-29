type UserInfoProps = {
    givenName?: string;
    familyName?: string;
    email?: string;
};

export const UserInfo = ({ givenName, familyName, email }: UserInfoProps) => {
    return (
        <div className="flex-1">
            <h2 className="text-2xl md:text-3xl font-medium text-gray-800 mb-2">
                {givenName} {familyName}
            </h2>
            <p className="text-gray-600 font-light mb-3">
                {email}
            </p>

            <div className="flex flex-wrap gap-3">
                <div className="bg-kinri-soft px-4 py-2 rounded-xl flex items-center gap-2">
                    <i className="fas fa-calendar-check text-kinri-primary"></i>
                    <span className="text-kinri-primary font-medium">
                        3 sessions completed
                    </span>
                </div>
                <div className="bg-purple-50 px-4 py-2 rounded-xl flex items-center gap-2">
                    <i className="fas fa-clock text-purple-700"></i>
                    <span className="text-purple-700 font-medium">
                        Last session: 2 days ago
                    </span>
                </div>
            </div>
        </div>
    );
};

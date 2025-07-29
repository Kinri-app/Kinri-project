import { useAssessmentStore } from '../store/assessmentStore';
import type { Option } from '../types/assessmentTypes';


export const AssessmentOption = ({
    value,
    label,
}: Option) => {
    const { currentOption, setOption } = useAssessmentStore();
    const isSelected = value === currentOption

    return (
        <button
            key={value}
            onClick={() => setOption(value)}
            className={`answer-option w-full p-4 text-left border-2 rounded-lg transition-all duration-300 cursor-pointer group ${isSelected
                ? 'border-[#876E2C] bg-[#876E2C]/10'
                : 'border-gray-200 hover:border-[#876E2C] hover:bg-[#876E2C]/5'
                }`}
            data-value={value}
        >
            <div className="flex items-center justify-between gap-1">
                <div>
                    <span
                        className={`font-medium ${isSelected ? 'text-[#876E2C]' : 'text-gray-800'
                            } group-hover:text-[#876E2C]`}
                    >
                        {label}
                    </span>
                </div>
                <i
                    className={`check-icon fas ${isSelected
                        ? 'fa-check-circle text-[#876E2C]'
                        : 'fa-circle text-gray-300'
                        } group-hover:text-[#876E2C] duration-300`}
                ></i>
            </div>
        </button>
    );
};

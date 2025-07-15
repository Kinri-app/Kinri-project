import axios from "axios";

const API_URL = "http://localhost:5001/api";

export const getAssessmentQuestions = async (
    getAccessTokenSilently: () => Promise<string>
) => {
    try {
        const token = await getAccessTokenSilently();
        const response = await axios.get(
            `${API_URL}/assessments/assessment_questions`,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            }
        );
        return response.data;
    } catch (error: any) {
        const message =
            error?.response?.data?.developerMessage ||
            error?.response?.data?.message ||
            "Failed to fetch assessment questions";
        throw new Error(message);
    }
};

export const getConditionWeights = async (
    getAccessTokenSilently: () => Promise<string>
) => {
    try {
        const token = await getAccessTokenSilently();
        const response = await axios.get(
            `${API_URL}/assessments/condition_weights`,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            }
        );
        return response.data;
    } catch (error: any) {
        const message =
            error?.response?.data?.developerMessage ||
            error?.response?.data?.message ||
            "Failed to fetch condition weights";
        throw new Error(message);
    }
}; 
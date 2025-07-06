from app.questions import questions_bp


@questions_bp("/", methods=['GET'])
def return_questionnaire():
    questionnaire()


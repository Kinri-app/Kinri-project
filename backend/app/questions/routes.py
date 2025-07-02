from app.questions import questions_bp
from flask import request, jsonify
from app.models import AssessmentQuestion, db
from sqlalchemy import select
from marshmallow import ValidationError
from utils.utils import questionnaire
from app.questions.schemas import assessment_question_schema, assessment_questions_schema




# ---------------------Route to assessment questionnaire-------------------------

@questions_bp("/", methods=['GET'])
def return_questionnaire():
    questionnaire()


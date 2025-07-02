from app.models import AssessmentQuestion
from app.extensions import ma

class AssessmentQuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AssessmentQuestion

assessment_question_schema = AssessmentQuestionSchema()
assessment_questions_schema = AssessmentQuestionSchema(many=True)


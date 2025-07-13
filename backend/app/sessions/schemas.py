from app.extensions import ma
from models import UserSessions

class SessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserSessions

session_schema = SessionSchema() 
sessions_schema = SessionSchema(many=True)
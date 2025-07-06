from app.models import MistralChat
from app.extensions import ma

class MistralChatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MistralChat


mistralchat_schema = MistralChatSchema()
mistralchats_schema = MistralChatSchema(many=True)
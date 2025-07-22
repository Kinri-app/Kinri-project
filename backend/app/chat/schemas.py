from app.models import MistralChat
from app.extensions import ma

class ChatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MistralChat


chat_schema = ChatSchema()
chats_schema = ChatSchema(many=True)
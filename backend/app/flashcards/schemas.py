from app.models import Flashcard
from app.extensions import ma

class FlashcardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Flashcard


flashcard_schema = FlashcardSchema()
flashcards_schema = FlashcardSchema(many=True)

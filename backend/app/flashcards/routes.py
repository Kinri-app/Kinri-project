from app.flashcards import flashcards_bp
from app.flashcards.schemas import flashcard_schema, flashcards_schema
from flask import request, jsonify
from app.models import Flashcard, db
from sqlalchemy import select
from marshmallow import ValidationError

# --------------Flashcard routes------------------------------

# Function to return all flashcards
@flashcards_bp.route("/", methods=["GET"])
def get_flashcards():
    query = select(Flashcard)
    result = db.session.execute(query).scalars().all()

    return flashcards_schema.jsonify(result), 200

# Function to return single flashcard by it's ID
@flashcards_bp("/<int:flashcard_id")
def get_flashcard_by_id(flashcard_id):
    try:
        query = select(Flashcard).where(Flashcard.id == flashcard_id)
        single_flashcard = db.session.execute(query)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    db.session.commit()
    
    return jsonify(single_flashcard)

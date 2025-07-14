from flask import request, jsonify, Blueprint
from sqlalchemy import select
from app import supabase

flashcards_bp = Blueprint('flashcards_bp',__name__)

# --------------Flashcard routes------------------------------

# Function to return all flashcards
@flashcards_bp.route("/", methods=["GET"])
def get_flashcards():
    try:
        response = supabase.table("tier1_2_batch1").select("*").execute()

        if not response.data:
            return jsonify({"error": "Failed to retrieve supabase data."}), 404
        
        # Transform the data to match frontend expectations
        flashcards = []
        for row in response.data:
            flashcard = {
                "question": row.get("Symptom", ""),
                "answer": row.get("Echo-Friendly Description", ""),
                "tags": [row.get("Tier", "")] if row.get("Tier") else [],
                "weights": row.get("Sample Weights", "")
            }
            flashcards.append(flashcard)
        
        return jsonify(flashcards)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
        
        return jsonify(response.data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

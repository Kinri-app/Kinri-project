from flask import request, jsonify, Blueprint
from sqlalchemy import select
from app import supabase

flashcards_bp = Blueprint('flashcards_bp',__name__)

# --------------Flashcard routes------------------------------

# Function to return all flashcards
@flashcards_bp.route("/", methods=["GET"])
def get_flashcards():
    try:
        response = supabase.table("flashcards").select("*").execute()

        if not response.data:
            return jsonify({"error": "Failed to retrieve supabase data."}), 404
        
        return jsonify(response.data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@flashcards_bp.route("/", methods=["POST"])
def create_flashcards():
    try:
        data = request.get_json()

        # Validate required fields
        if not data or not all(k in data for k in ("question", "answer", "tags")):
            return jsonify({"error": "Missing required flashcard fields."}), 400

        response = supabase.table("flashcards").insert(data).execute()

        return jsonify(response.data), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Route to post batch flashcards and account for the variance in headline showing up
@flashcards_bp.route("/batch", methods=["POST"])
def create_flashcards_batch():
    try:
        data = request.get_json()

        if not data or not isinstance(data, list):
            return jsonify({"error": "A list of flashcards is required"}), 400

        insert_data = []

        for card in data:
            # Skip non-flashcards
            if card.get("card_type") != "flashcard":
                continue

            # Validate required fields
            required_keys = ["card_id", "question", "answer", "tags"]
            if not all(k in card for k in required_keys):
                return jsonify({"error": f"Missing fields in flashcard: {card.get('card_id', 'unknown')}"}), 400

            tags = card["tags"]

            insert_data.append({
                "card_id": card["card_id"],
                "question": card["question"],
                "answer": card["answer"],
                "condition": tags.get("condition", []),
                "emotion": tags.get("emotion", []),
                "narrative_type": tags.get("narrative_type", []),
                "usage_mode": tags.get("usage_mode", [])
            })

        if not insert_data:
            return jsonify({"message": "No flashcards found to insert."}), 200

        response = supabase.table("flashcards").insert(insert_data).execute()

        if response.error:
            return jsonify({"error": response.error.message}), 500

        return jsonify({"message": "Flashcards inserted successfully", "count": len(insert_data)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

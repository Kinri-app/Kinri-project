from flask import request, Blueprint
from app import supabase
from app.utils.responses import standard_response

flashcards_bp = Blueprint('flashcards_bp', __name__)

# ------------------ GET ALL FLASHCARDS ------------------

@flashcards_bp.route("/", methods=["GET"])
def get_flashcards():
    try:
        response = supabase.table("flashcards").select("*").execute()

        if not response.data:
            return standard_response(
                status="OK",
                status_code=200,
                message="No flashcards found.",
                data=[]
            )

        return standard_response(
            status="OK",
            status_code=200,
            message="Flashcards retrieved successfully.",
            data=response.data
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Failed to retrieve flashcards.",
            reason="Database query error",
            developer_message=str(e)
        )

# ------------------ POST SINGLE FLASHCARD ------------------

@flashcards_bp.route("/", methods=["POST"])
def create_flashcard():
    try:
        data = request.get_json()

        if not data or not all(k in data for k in ("question", "answer", "tags")):
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="Missing required flashcard fields.",
                reason="Expected keys: 'question', 'answer', 'tags'",
                developer_message=f"Payload received: {data}"
            )

        response = supabase.table("flashcards").insert(data).execute()

        if response.error:
            return standard_response(
                status="INTERNAL_SERVER_ERROR",
                status_code=500,
                message="Flashcard insert failed.",
                developer_message=response.error.message
            )

        return standard_response(
            status="OK",
            status_code=201,
            message="Flashcard created successfully.",
            data=response.data
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An unexpected error occurred during flashcard creation.",
            developer_message=str(e)
        )

# ------------------ POST FLASHCARDS IN BATCH ------------------

@flashcards_bp.route("/batch", methods=["POST"])
def create_flashcards_batch():
    try:
        data = request.get_json()

        if not data or not isinstance(data, list):
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="A list of flashcards is required.",
                reason="Missing or invalid JSON list",
                developer_message="Expected a JSON array of flashcard objects"
            )

        insert_data = []

        for card in data:
            if card.get("card_type") != "flashcard":
                continue

            required_keys = ["card_id", "question", "answer", "tags"]
            if not all(k in card for k in required_keys):
                return standard_response(
                    status="BAD_REQUEST",
                    status_code=400,
                    message="Missing fields in flashcard.",
                    reason="Required fields: card_id, question, answer, tags",
                    developer_message=f"Card with issues: {card}"
                )

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
            return standard_response(
                status="OK",
                status_code=200,
                message="No valid flashcards found to insert.",
                data=[]
            )

        response = supabase.table("flashcards").insert(insert_data).execute()

        if response.error:
            return standard_response(
                status="INTERNAL_SERVER_ERROR",
                status_code=500,
                message="Batch flashcard insert failed.",
                developer_message=response.error.message
            )

        return standard_response(
            status="OK",
            status_code=201,
            message="Flashcards inserted successfully.",
            data={"inserted_count": len(insert_data)}
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An error occurred while processing batch flashcards.",
            developer_message=str(e)
        )

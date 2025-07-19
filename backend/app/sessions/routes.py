from flask import request, jsonify, Blueprint, g
from sqlalchemy import select
from app import supabase
from app.auth.decorators import requires_auth
from app.chat.utils import ask_mistral
from app.utils.utils import cleanup_old_sessions

sessions_bp = Blueprint('sessions_bp',__name__)

# --------------Flashcard routes------------------------------

# route to return all recorder sessions of the user
@sessions_bp.route("/<user_id>", methods=["GET"])
@requires_auth
def get_user_sessions(id):
    pass



# Once the session is complete it will update the session table to include the conversation
@sessions_bp.route("/complete", methods=["POST"])
@requires_auth
def complete_session(session_id):
    data = request.get_json()
    full_chat_history = data.get("conversation")

    if not full_chat_history:
        return jsonify({"error": "Missing conversation text"}), 400

    user_id = g.current_user["id"]

    data = request.get_json()
    full_chat_history = data.get("conversation")

    if not full_chat_history:
        return jsonify({"error": "Missing conversation text"}), 400

    # 1. Prepare emotion inference prompt
    prompt = f"""
        Based on the full conversation below, infer the user's dominant emotional state(s).

        Use this emotion list: ["joy", "sadness", "anger", "fear", "trust", "disgust", "surprise", "anticipation"]

        Return a JSON object like:
        {{
        "emotions": ["fear", "sadness"],
        "intensity": "moderate",
        "confidence": 0.87
        }}

        Chat history:
        {full_chat_history}
    """

    try:
        model = "open-mistral-7b"
        reply, _ = ask_mistral(prompt, [], model)
        vault_card_id = data.get("vault_card_id")

        # 2. Extract JSON object from Mistral response
        import re, json


        def extract_first_json(text):
            """
            Extracts the first valid JSON object from a string containing one or more {...} blocks.
            Returns the parsed JSON as a Python dict, or None if no valid JSON is found.
            """
            matches = re.findall(r"\{.*?\}", text, re.DOTALL)  # non-greedy
            for match in matches:
                try:
                    return json.loads(match)
                except json.JSONDecodeError:
                    continue
            return None

        emotion_data = extract_first_json(reply)

        # 3. Structure update payload
        update_payload = {
            "conversation": full_chat_history,
            "user_id": user_id,
            "user_emotions": ", ".join(emotion_data.get("emotions", [])),
            "emotional_intensity": emotion_data.get("intensity"),
            "llm_confidence": emotion_data.get("confidence"),
        }

        if vault_card_id:
            update_payload["vault_card_id"] = vault_card_id

        # 4. Update Supabase session
        response = supabase.table("sessions").update(update_payload).eq("id", session_id).execute()

        if response.error:
            return jsonify({"error": response.error.message}), 500

        return jsonify({"message": "Session completed", "emotions": emotion_data}), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Internal error", "detail": str(e)}), 5000

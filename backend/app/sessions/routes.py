from flask import request, Blueprint, jsonify, g
from app import supabase
from app.auth.decorators import requires_auth
from app.chat.utils import ask_mistral
from app.core.utils import standard_response
from app.utils.utils import cleanup_old_sessions  # make sure this exists

import json
import re

sessions_bp = Blueprint("sessions_bp", __name__)

@sessions_bp.route("/complete", methods=["POST"])
@requires_auth
def complete_session():
    try:
        data = request.get_json()
        full_chat_history = data.get("conversation")
        vault_card_id = data.get("associated_vault_card_id")


        if not full_chat_history:
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="Missing required fields",
                reason="Missing conversation text or session ID",
                developer_message="Ensure 'conversation' is included in the request."
            )

        user_id = g.current_user["id"]

        # 1. Generate prompt for emotion detection
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

        model = "open-mistral-7b"
        reply, _ = ask_mistral(prompt, [], model)

        # 2. Extract the JSON object from the model reply
        def extract_first_json(text):
            matches = re.findall(r"\{.*?\}", text, re.DOTALL)
            for match in matches:
                try:
                    return json.loads(match)
                except json.JSONDecodeError:
                    continue
            return {}

        emotion_data = extract_first_json(reply)

        # 3. Prepare session update payload
        update_payload = {
            "conversation": full_chat_history,
            "user_id": user_id,
            "user_emotions": ", ".join(emotion_data.get("emotions", [])),
            "emotional_intensity": emotion_data.get("intensity"),
            "llm_confidence": emotion_data.get("confidence")
        }

        if vault_card_id:
            update_payload["associated_vault_card_id"] = vault_card_id

        # 4. Update session in Supabase
        response = supabase.table("sessions").insert(update_payload).execute()

        if not response.data:
            return standard_response(
                status="INTERNAL_SERVER_ERROR",
                status_code=500,
                message="Supabase update failed",
                reason="Session insert returned no data",
                developer_message=f"Status code: {response.status_code}"
            )

        # 5. Cleanup old sessions if over limit
        cleanup_old_sessions(user_id)

        return standard_response(
            status="OK",
            status_code=200,
            message="Session completed and emotion recorded.",
            data={"emotions": emotion_data}
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Unexpected error occurred during session completion.",
            reason="Unhandled exception",
            developer_message=str(e)
        )
    




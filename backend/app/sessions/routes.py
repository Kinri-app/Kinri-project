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


        if not full_chat_history:
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="Missing required fields",
                reason="Missing conversation text or session ID",
                developer_message="Ensure 'conversation' is included in the request."
            )

        auth0_id = g.current_user["auth0_id"]

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
        Also, based on the vault card data you selected please return the associated id in the following format.
        Return only a JSON object in the following format:
        {{ "id": <the id of the selected vault card> }}

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

        
        def extract_card_id(text):
            match = re.search(r'"id":\s*(\d+)', text)
            return int(match.group(1)) if match else None
        
        associated_vault_card_id = extract_card_id(reply)

        # 3. Prepare session update payload
        update_payload = {
            "auth0_id": auth0_id,
            "conversation": full_chat_history,
            "user_emotions": ", ".join(emotion_data.get("emotions", [])),
            "emotional_intensity": emotion_data.get("intensity"),
            "llm_confidence": emotion_data.get("confidence")
        }

        if associated_vault_card_id:
            update_payload["associated_vault_card_id"] = associated_vault_card_id

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
        cleanup_old_sessions(auth0_id)

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
    


@sessions_bp.route("/conversations", methods=["GET"])
@requires_auth
def get_previous_user_conversations():
    try:
        auth0_id = g.current_user["auth0_id"]

        response = (
            supabase
            .table("sessions")
            .select("conversation")
            .eq("auth0_id", auth0_id)
            .order("created_at", desc=True)  # Optional: show most recent first
            .execute()
        )

        if not response.data:
            return standard_response(
                status="OK",
                status_code=200,
                message="No previous data found.",
                data=[]
            )

        return standard_response(
            status="OK",
            status_code=200,
            message="Previous sessions retrieved successfully.",
            data=response.data
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Failed to retrieve previous sessions.",
            reason="Database query error",
            developer_message=str(e)
        )
    
@sessions_bp.route("/", methods=["GET"])
@requires_auth
def get_all_sessions_data():
    try:
        auth0_id = g.current_user["auth0_id"]

        response = (
            supabase
            .table("sessions")
            .select("*")
            .eq("auth0_id", auth0_id)
            .order("created_at", desc=True)  # Optional: show most recent first
            .execute()
        )

        if not response.data:
            return standard_response(
                status="OK",
                status_code=200,
                message="No previous data found.",
                data=[]
            )

        return standard_response(
            status="OK",
            status_code=200,
            message="Previous sessions retrieved successfully.",
            data=response.data
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Failed to retrieve previous sessions.",
            reason="Database query error",
            developer_message=str(e)
        )
        
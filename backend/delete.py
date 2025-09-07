from flask import Blueprint, request, jsonify, g
from app import supabase
from app.auth.decorators import requires_auth
from app.chat.utils import ask_mistral
from app.core.utils import standard_response

sessions_bp = Blueprint("sessions_bp", __name__)

@sessions_bp.route("/<session_id>/complete", methods=["PUT"])
@requires_auth
def complete_session(session_id):
    data = request.get_json()
    text = data.get("conversation")
    vault_card_id = data.get("vault_card_id")  # optional

    if not text:
        return standard_response(
            status="BAD_REQUEST",
            status_code=400,
            message="Missing conversation data.",
            reason="Field 'conversation' is required in the request body.",
            developer_message="Ensure the frontend sends a JSON object with the key 'conversation'."
        )

    user_id = g.current_user["id"]

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
    {text}
    """

    try:
        model = "open-mistral-7b"
        reply, _ = ask_mistral(prompt, [], model)

        # 2. Extract JSON object from Mistral response
        import re, json

        def extract_json(text):
            try:
                match = re.search(r"\{.*\}", text, re.DOTALL)
                return json.loads(match.group(0)) if match else {}
            except Exception as e:
                print("Error parsing emotion JSON:", e)
                return {}

        emotion_data = extract_json(reply)

        # 3. Structure update payload
        update_payload = {
            "conversationt": text,
            "user_id": user_id,
            "user_emotion": ", ".join(emotion_data.get("emotions", [])),
            "emotional_intensity": emotion_data.get("intensity"),
            "llm_confidence": emotion_data.get("confidence"),
        }

        if vault_card_id:
            update_payload["vault_card_id"] = vault_card_id

        # 4. Update Supabase session
        response = supabase.table("sessions").update(update_payload).eq("id", session_id).execute()

        if response.error:
            return standard_response(
                status="INTERNAL_SERVER_ERROR",
                status_code=500,
                message="Failed to update session.",
                reason="Supabase returned an error.",
                developer_message=response.error.message
            )
        return standard_response(
            status="OK",
            status_code=200,
            message="Session completed successfully.",
            data={"emotions": emotion_data}
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Unexpected error during session completion.",
            reason="Unhandled exception.",
            developer_message=str(e)
        )

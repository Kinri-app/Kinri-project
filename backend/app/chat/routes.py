from flask import request, Blueprint
from datetime import datetime, timezone
from app.core.utils import standard_response
from app.chat.utils import ask_mistral
from app.auth.decorators import requires_auth


chat_bp = Blueprint("chat_bp", __name__)


@chat_bp.route("/", methods=["POST"])
@requires_auth
def chat():
    data = request.json
    message = data.get("message")
    history = data.get("history", [])
    model = "open-mistral-7b"

    if not message:
        return standard_response(
            status="BAD_REQUEST",
            status_code=400,
            message="The 'message' field is required.",
            reason="Missing message in request body",
            developer_message="Ensure the client sends a 'message' key in the JSON payload.",
        )

    try:
        reply, updated_history = ask_mistral(message, history, model)

        return standard_response(
            status="OK",
            status_code=200,
            message="Chat response generated successfully.",
            data={"reply": reply, "history": updated_history},
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Something went wrong while generating the response.",
            reason="Chat processing error",
            developer_message=str(e),
        )

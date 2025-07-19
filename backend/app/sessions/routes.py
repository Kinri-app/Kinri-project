from flask import request, jsonify, Blueprint, g
from sqlalchemy import select
from app import supabase
from app.auth.decorators import requires_auth

sessions_bp = Blueprint('sessions_bp',__name__)

# --------------Flashcard routes------------------------------

# Function to return all flashcards
@sessions_bp.route("/<user_id>", methods=["GET"])
@requires_auth
def get_user_sessions(id):
    pass





@sessions_bp.route("/", methods=["POST"])
@requires_auth
def create_user_session():
    user_id = g.current_user["sub"]

    response = supabase.table("session").insert({
        "user_id": user_id,
        "text": ""
    }).execute()

    if response.error:
        return jsonify({"error": response.error.message}), 500
    
    return jsonify({"session_id": response.data[0]["id"]}), 201


# Once the session is complete it will update the session table to include the conversation
@sessions_bp.route("/<session_id>/complete", methods=["PUT"])
@requires_auth
def update_session_text(session_id):
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "Missing conversation text"}), 400

    response = supabase.table("session").update({
        "text": text
    }).eq("id", session_id).execute()

    if response.error:
        return jsonify({"error": response.error.message}), 500

    return jsonify({"message": "Session updated"}), 200

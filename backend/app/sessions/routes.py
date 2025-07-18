from flask import request, jsonify, Blueprint
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
    pass
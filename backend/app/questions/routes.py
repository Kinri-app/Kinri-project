from flask import request, Blueprint, jsonify
from datetime import datetime, timezone
from app import supabase

questions_bp = Blueprint('questions_bp', __name__)

@questions_bp.route("/", methods=["GET"])
def get_assessment_questions():
    try:
        response = supabase.table("assessment_questions").select("*").execute()

        if not response.data:
            return jsonify({"error": "Failed to retrieve supabase data."}), 404
        
        return jsonify(response.data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
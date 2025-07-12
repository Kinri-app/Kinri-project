from flask import request, Blueprint, jsonify
from datetime import datetime, timezone
from app import supabase
from collections import defaultdict

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
    
@questions_bp.route("/condition_weights", methods=["GET"])
def get_questions_conditions_weights():
    try:
        response = supabase.table("question_condition_weighting") \
        .select("question_id, weight, assessment_questions(question), conditions(name)") \
        .execute()
    
        rows = response.data

        # If you access a key that doesn't exist, it automatically creates this structure: {"question": "", "conditions": {}} 
        grouped = defaultdict(lambda: {"question": "", "conditions": {}}) #defaultdict allows us to bypass if key not in group logic, it autocreates if not there and then appends to already existing keys

        for row in rows:
            question_text = row["assessment_questions"]["question"]
            condition_name = row["conditions"]["name"]
            weight = row["weight"]

            grouped[question_text]["question"] = question_text #Creates "question":"this is a sample question"
            grouped[question_text]["conditions"][condition_name] = weight #creates "conditions": {"CPTSD": 1, "GAD": 0.5, "PTSD": 0.5}

        # Convert defaultdict to list
        result = list(grouped.values()) #Converts it to a list of objects in json format
        return jsonify(result), 200

    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"error": str(e)}), 500

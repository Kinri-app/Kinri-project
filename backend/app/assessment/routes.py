from flask import Blueprint, request, jsonify
from app import supabase
from app.utils.assessment import calculate_condition_scores
from datetime import datetime, timezone
from collections import defaultdict


assessment_bp = Blueprint('assessment_bp', __name__)

@assessment_bp.route("/calculate_scores", methods=["POST"])
def calculate_scores():
    try:
        # 1. Get responses from frontend
        user_responses = request.get_json()

        if not user_responses or not isinstance(user_responses, list):
            return jsonify({"error": "Invalid input format"}), 400

        # 2. Get question-condition-weight mappings from Supabase
        response = supabase.table("question_condition_weighting") \
            .select("id, weight, assessment_questions(id), conditions(name)") \
            .execute()

        # 3. Transform Supabase flat rows into nested format
        raw_rows = response.data
        question_map = {}

        for row in raw_rows:
            question_id = row["assessment_questions"]["id"]
            condition = row["conditions"]["name"]
            weight = row["weight"]

            if question_id not in question_map:
                question_map[question_id] = {
                    "id": question_id,
                    "conditions": {}
                }

            question_map[question_id]["conditions"][condition] = weight

        question_weights = list(question_map.values())

        # 4. Calculate condition scores
        scores = calculate_condition_scores(user_responses, question_weights)

        # 5. Return the scores to frontend
        return jsonify(scores), 200

    except Exception as e:
        print("Error in assessment route:", str(e))
        return jsonify({"error": str(e)}), 500


@assessment_bp.route("/assessment_questions", methods=["GET"])
def get_assessment_questions():
    try:
        response = supabase.table("assessment_questions").select("*").execute()

        if not response.data:
            return jsonify({"error": "Failed to retrieve supabase data."}), 404
        
        return jsonify(response.data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@assessment_bp.route("/condition_weights", methods=["GET"])
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

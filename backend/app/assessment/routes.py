from flask import Blueprint, request, jsonify
from app import supabase
from app.utils.assessment import calculate_condition_scores


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

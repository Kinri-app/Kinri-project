from flask import Blueprint, request, jsonify
from app import supabase
from app.chat.utils import ask_mistral
from app.core.utils import standard_response
from app.utils.assessment import calculate_condition_scores
from datetime import datetime, timezone
from collections import defaultdict


assessment_bp = Blueprint("assessment_bp", __name__)


@assessment_bp.route("/evaluate", methods=["POST"])
def evaluate():

    try:
        # data = request.json
        # # history = data.get("history", [])
        model = "open-mistral-7b"

        # 1. Get responses from frontend
        user_responses = request.get_json()

        if not user_responses or not isinstance(user_responses, list):
            return jsonify({"error": "Invalid input format"}), 400

        # 2. Get question-condition-weight mappings from Supabase
        response = (
            supabase.table("question_condition_weighting")
            .select("id, weight, assessment_questions(id), conditions(name)")
            .execute()
        )

        # 3. Transform Supabase flat rows into nested format
        raw_rows = response.data
        question_map = {}

        for row in raw_rows:
            question_id = row["assessment_questions"]["id"]
            condition = row["conditions"]["name"]
            weight = row["weight"]

            if question_id not in question_map:
                question_map[question_id] = {"id": question_id, "conditions": {}}

            question_map[question_id]["conditions"][condition] = weight

        question_weights = list(question_map.values())

        # 4. Calculate condition scores
        scores = calculate_condition_scores(user_responses, question_weights)

        prompt = """
                "The user has just completed a mental health assessment.\n"
                "You will be shown a list of related educational vault cards. Each contains a question and an answer.\n"
                "You are the users understanding companion that does not wish to impose but would like to offer some information if they want it.\n"
                "Let them know that one assessment cannot understand all of the intracicies that make them up.\n"
                "Based on the user's highest scored condition, pick ONE vault card that best reflects their likely concern.\n"
                "Do not bring up seeking help from professionals only that if they are interested in learning more you are there for them.\n"
                "Ask the question associated with the Symptom key and follow it up with the description associated with the Echo friendly description key\n"
                """

        vault_table_data = (
            supabase.table("Kinri_Symptom_Prompts_With_Vault_Tags")
            .select("*")
            .execute()
        )

        system_message = (
            f"Assessment Results:\n{scores}\n\n"
            f"Vault Table Data:\n{vault_table_data}\n\n"
            f"Instructions:\n{prompt}"
        )

        # 5. Return the scores to frontend
        reply, updated_history = ask_mistral(system_message, [], model)

        return standard_response(
            status="OK",
            status_code=200,
            message="Chat response generated successfully.",
            data={"reply": reply, "history": updated_history},
        )

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
        response = (
            supabase.table("question_condition_weighting")
            .select(
                "question_id, weight, assessment_questions(question), conditions(name)"
            )
            .execute()
        )

        rows = response.data

        # If you access a key that doesn't exist, it automatically creates this structure: {"question": "", "conditions": {}}
        grouped = defaultdict(
            lambda: {"question": "", "conditions": {}}
        )  # defaultdict allows us to bypass if key not in group logic, it autocreates if not there and then appends to already existing keys

        for row in rows:
            question_text = row["assessment_questions"]["question"]
            condition_name = row["conditions"]["name"]
            weight = row["weight"]

            grouped[question_text][
                "question"
            ] = question_text  # Creates "question":"this is a sample question"
            grouped[question_text]["conditions"][
                condition_name
            ] = weight  # creates "conditions": {"CPTSD": 1, "GAD": 0.5, "PTSD": 0.5}

        # Convert defaultdict to list
        result = list(
            grouped.values()
        )  # Converts it to a list of objects in json format
        return jsonify(result), 200

    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"error": str(e)}), 500

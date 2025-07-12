from app import supabase
from flask import Blueprint, request, jsonify

vaultcards_bp = Blueprint('vaultcards_bp', __name__)
# -------------------Vaultcard Routes--------------------------

# Function to return all vault cards
@vaultcards_bp.route("/", methods=["GET"])
def get_vaultcards():

    try:
        # 2. Get question-condition-weight mappings from Supabase
        response = supabase.table("tier1_2_batch1").select('Symptom, "Echo-Friendly Description", Tier, "Sample Weights"').execute()

        # 3. Transform Supabase flat rows into nested format
        raw_rows = response.data
        vaultcard_map = {}

        for row in raw_rows:
            symptom = row["Symptom"]
            description = row["Echo-Friendly Description"]
            tier = row["Tier"]
            weights = row["Sample Weights"]

            if symptom not in vaultcard_map:
                vaultcard_map[symptom] = {
                    "symptom": symptom,
                    "description": description,
                    "tier": tier,
                    "weights": weights
                }

        vaultcards = list(vaultcard_map.values())


        # 5. Return the scores to frontend
        return jsonify(vaultcards), 200
    
    except Exception as e:
        print("Error in assessment route:", str(e))
        return jsonify({"error": str(e)}), 500


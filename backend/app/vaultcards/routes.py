from app import supabase
from flask import Blueprint, request, jsonify
from app.utils.utils import flatten_tags

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

@vaultcards_bp.route("/", methods=["POST"])
def create_vault_card():
    try:
        data = request.get_json()

        if not data or not all(k in data for k in ("card_id", "card_type", "headline", "body", "prompt", "tags")):
            return jsonify({"error": "Missing required vault card fields."}), 400

        tags = data["tags"]

        # Flatten tags into their own columns
        insert_data = {
            "card_id": data["card_id"],
            "card_type": data["card_type"],
            "headline": data["headline"],
            "body": data["body"],
            "prompt": data["prompt"],
            "condition": tags.get("condition", []),
            "emotion": tags.get("emotion", []),
            "narrative_type": tags.get("narrative_type", []),
            "usage_mode": tags.get("usage_mode", [])
        }

        response = supabase.table("vault_cards").insert(insert_data).execute()

        return jsonify(response.data), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# This route is designed to insert vault cards based on the data provided by Kinri in mass
@vaultcards_bp.route("/batch", methods=["POST"])
def add_vaultcard_batch():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided."}), 400

        # Normalize to list
        cards = data if isinstance(data, list) else [data]

        insert_data = []

        for card in cards:
            if not all(k in card for k in ("card_id", "card_type", "headline", "body", "prompt", "tags")):
                return jsonify({"error": f"Missing fields in card: {card.get('card_id', 'unknown')}"}), 400

            tags = card["tags"]
            insert_data.append({
                "card_id": card["card_id"],
                "card_type": card["card_type"],
                "headline": card["headline"],
                "body": card["body"],
                "prompt": card["prompt"],
                "condition": tags.get("condition", []),
                "emotion": tags.get("emotion", []),
                "narrative_type": tags.get("narrative_type", []),
                "usage_mode": tags.get("usage_mode", [])
            })

        response = supabase.table("vault_cards").insert(insert_data).execute()

        if response.error:
            return jsonify({"error": response.error.message}), 500

        return jsonify({"message": "Vault cards inserted", "data": response.data}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
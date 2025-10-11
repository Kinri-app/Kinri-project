from flask import request, Blueprint
from app import supabase
from app.utils.responses import standard_response
import ast, json
from typing import Any, Dict, List

flashcards_bp = Blueprint('flashcards_bp', __name__)

# ------------------ GET ALL FLASHCARDS ------------------

@flashcards_bp.route("/", methods=["GET"])
def get_flashcards():
    try:
        response = supabase.table("flashcards").select("*").execute()

        if not response.data:
            return standard_response(
                status="OK",
                status_code=200,
                message="No flashcards found.",
                data=[]
            )

        return standard_response(
            status="OK",
            status_code=200,
            message="Flashcards retrieved successfully.",
            data=response.data
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="Failed to retrieve flashcards.",
            reason="Database query error",
            developer_message=str(e)
        )

# ------------------ POST SINGLE FLASHCARD ------------------

@flashcards_bp.route("/", methods=["POST"])
def create_flashcard():
    try:
        data = request.get_json()

        if not data or not all(k in data for k in ("question", "answer", "tags")):
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="Missing required flashcard fields.",
                reason="Expected keys: 'question', 'answer', 'tags'",
                developer_message=f"Payload received: {data}"
            )

        response = supabase.table("flashcards").insert(data).execute()

        if response.error:
            return standard_response(
                status="INTERNAL_SERVER_ERROR",
                status_code=500,
                message="Flashcard insert failed.",
                developer_message=response.error.message
            )

        return standard_response(
            status="OK",
            status_code=201,
            message="Flashcard created successfully.",
            data=response.data
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An unexpected error occurred during flashcard creation.",
            developer_message=str(e)
        )

# ------------------ POST FLASHCARDS IN BATCH ------------------

from postgrest import APIError  # supabase-py raises this for DB errors

@flashcards_bp.route("/batch", methods=["POST"])
def create_flashcards_batch():
    try:
        data = request.get_json()

        if not isinstance(data, list):
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="A list of flashcards is required.",
                reason="Missing or invalid JSON list",
                developer_message="Expected a JSON array of flashcard objects"
            )

        insert_data = []
        for card in data:
            if card.get("card_type") != "flashcard":
                continue

            required_keys = ["card_id", "question", "answer", "tags"]
            if not all(k in card for k in required_keys):
                return standard_response(
                    status="BAD_REQUEST",
                    status_code=400,
                    message="Missing fields in flashcard.",
                    reason="Required fields: card_id, question, answer, tags",
                    developer_message=f"Card with issues: {card}"
                )

            tags = card.get("tags") or {}
            if not isinstance(tags, dict):
                tags = {}

            insert_data.append({
                "card_id": card["card_id"],
                "question": card["question"],
                "answer": card["answer"],
                "condition": tags.get("condition", []),
                "emotion": tags.get("emotion", []),
                "narrative_type": tags.get("narrative_type", []),
                "usage_mode": tags.get("usage_mode", []),
            })

        if not insert_data:
            return standard_response(
                status="OK",
                status_code=200,
                message="No valid flashcards found to insert.",
                data=[]
            )

        # Upsert: skip duplicates on card_id, insert only new rows.
        resp = supabase.table("flashcards").upsert(
            insert_data,
            on_conflict="card_id",
            ignore_duplicates=True,          # <- silently skip existing card_id
            returning="representation"       # <- so we can count inserted rows
        ).execute()

        inserted = len(resp.data) if getattr(resp, "data", None) is not None else None
        skipped = (len(insert_data) - inserted) if inserted is not None else None

        return standard_response(
            status="CREATED",
            status_code=201,
            message="Flashcards processed successfully (duplicates skipped).",
            data={
                "attempted": len(insert_data),
                "inserted": inserted,
                "skipped_duplicates": skipped
            }
        )

    except APIError as e:
        # Constraint/RLS/type errors surface here
        return standard_response(
            status="BAD_REQUEST",
            status_code=400,
            message="Batch flashcard upsert failed.",
            developer_message=str(e)
        )
    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An error occurred while processing batch flashcards.",
            developer_message=str(e)
        )

@flashcards_bp.route("/batch_discord_data", methods=["POST"])
def input_discord_data():
    try:
        data = request.get_json()

        if not isinstance(data, list):
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="A list of flashcards is required.",
                reason="Missing or invalid JSON list",
                developer_message="Expected a JSON array of flashcard objects"
            )

        insert_data = []
        for card in data:
            if card.get("card_type") != "flashcard":
                continue

            required_keys = ["card_id", "tags"]
            if not all(k in card for k in required_keys):
                return standard_response(
                    status="BAD_REQUEST",
                    status_code=400,
                    message="Missing fields in flashcard.",
                    reason="Required fields: card_id, question, answer, tags",
                    developer_message=f"Card with issues: {card}"
                )

            tags = card.get("tags") or {}
            if not isinstance(tags, dict):
                tags = {}

            insert_data.append({
                "card_id": card["card_id"],
                "question": card.get("question", []),
                "answer": card.get("answer", []),
                "condition": tags.get("condition", []),
                "emotion": tags.get("emotion", []),
                "narrative_type": tags.get("narrative_type", []),
                "usage_mode": tags.get("usage_mode", []),
                "headline": card.get("headline", []),
                "body": card.get("body", []),
                "prompt": card.get("prompt", [])
            })

        if not insert_data:
            return standard_response(
                status="OK",
                status_code=200,
                message="No valid flashcards found to insert.",
                data=[]
            )

        # Upsert: skip duplicates on card_id, insert only new rows.
        resp = supabase.table("discord_data_flash").upsert(
            insert_data,
            on_conflict="card_id",
            ignore_duplicates=True,          # <- silently skip existing card_id
            returning="representation"       # <- so we can count inserted rows
        ).execute()

        inserted = len(resp.data) if getattr(resp, "data", None) is not None else None
        skipped = (len(insert_data) - inserted) if inserted is not None else None

        return standard_response(
            status="CREATED",
            status_code=201,
            message="Flashcards processed successfully (duplicates skipped).",
            data={
                "attempted": len(insert_data),
                "inserted": inserted,
                "skipped_duplicates": skipped
            }
        )

    except APIError as e:
        # Constraint/RLS/type errors surface here
        return standard_response(
            status="BAD_REQUEST",
            status_code=400,
            message="Batch flashcard upsert failed.",
            developer_message=str(e)
        )
    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An error occurred while processing batch flashcards.",
            developer_message=str(e)
        )

@flashcards_bp.route("/batch_symptom_prompts", methods=["POST"])
def input_symptom_prompts():


    def coerce_sample_weights(val) -> Dict[str, float] | None:
        # Accept dict directly
        if isinstance(val, dict):
            return {str(k): float(v) for k, v in val.items()}
        # Accept string like "{'CPTSD': 0.5, 'Autism': 0.5}"
        if isinstance(val, str):
            s = val.strip()
            # try JSON (convert single quotes → double)
            try:
                j = json.loads(s.replace("'", '"'))
                if isinstance(j, dict):
                    return {str(k): float(v) for k, v in j.items()}
            except Exception:
                pass
            # try Python literal
            try:
                lit = ast.literal_eval(s)
                if isinstance(lit, dict):
                    return {str(k): float(v) for k, v in lit.items()}
            except Exception:
                pass
        return None

    try:
        data = request.get_json()

        # must be a non-empty list of dicts
        if not isinstance(data, list) or not data:
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="A non-empty list of prompts is required.",
                reason="Payload must be a JSON array of objects.",
                developer_message=f"type={type(data)} payload={data}"
            )

        required = {"symptom", "echo_friendly_description", "tier", "sample_weights"}

        insert_data: List[Dict[str, Any]] = []
        bad: List[Dict[str, Any]] = []

        for idx, item in enumerate(data):
            if not isinstance(item, dict):
                bad.append({"index": idx, "reason": "Item is not an object"})
                continue
            if not required.issubset(item.keys()):
                missing = list(required - set(item.keys()))
                bad.append({"index": idx, "reason": f"Missing keys: {missing}", "item": item})
                continue

            weights = coerce_sample_weights(item["sample_weights"])
            if weights is None:
                bad.append({"index": idx, "reason": "sample_weights not parseable (expect dict/JSON/stringified dict)", "value": item["sample_weights"]})
                continue

            # If your DB expects text for tier, leave as is (e.g., "Tier 3")
            # If it expects numeric tier, parse here:
            # tier_val = int(re.search(r'\d+', str(item["tier"])).group()) if re.search(r'\d+', str(item["tier"])) else item["tier"]

            insert_data.append({
                "symptom": item["symptom"],
                "echo_friendly_description": item["echo_friendly_description"],
                "tier": item["tier"],                 # keep as provided; change if DB expects int
                "sample_weights": weights,            # proper dict → JSONB
            })

        if not insert_data:
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="No valid items to insert.",
                reason="All items failed validation/parsing.",
                developer_message={"bad_items": bad}
            )

        resp = supabase.table("symptom_prompts_batch").insert(insert_data).execute()

        # supabase-py v2 typically exposes .data; .error may be None/absent
        if getattr(resp, "error", None):
            return standard_response(
                status="INTERNAL_SERVER_ERROR",
                status_code=500,
                message="Prompt batch failed.",
                developer_message=str(resp.error)
            )

        return standard_response(
            status="CREATED",
            status_code=201,
            message="Symptom prompts inserted successfully.",
            data={
                "attempted": len(data),
                "inserted": len(resp.data) if getattr(resp, "data", None) is not None else None,
                "skipped_invalid": len(bad),
                "invalid_items": bad[:5]  # preview first few
            }
        )

    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An unexpected error occurred during symptom prompt insert.",
            developer_message=str(e)
        )

@flashcards_bp.route("/submit_tone_palette", methods=["POST"])
def submit_tone_pallet():
    try:
        data = request.get_json()

            # must be a non-empty list of dicts
        if not isinstance(data, list) or not data:
            return standard_response(
                status="BAD_REQUEST",
                status_code=400,
                message="A non-empty list of data is required.",
                reason="Payload must be a JSON array of objects.",
                developer_message=f"type={type(data)} payload={data}"
            )
        
        required = {"tone", "used_for", "pacing", "language_style", "vault_types", "avoid"}

        insert_data: List[Dict[str, Any]] = []



        for item in data:
            if not all(k in item for k in required):
                return standard_response(
                    status="BAD_REQUEST",
                    status_code=400,
                    message="Missing fields in flashcard.",
                    reason="Required fields: card_id, question, answer, tags",
                    developer_message=f"Card with issues: {item}"
                )
            
            insert_data.append({
                "tone": item["tone"],
                "used_for": item["used_for"],
                "pacing": item["pacing"],
                "language_style": item["language_style"],
                "vault_types": item["vault_types"],
                "avoid": item["avoid"]
                })
        
        response = supabase.table("tone_pallete").upsert(insert_data).execute()
        
        return standard_response(
            status="OK",
            status_code=200,
            message=f"Upserted {len(insert_data)} tone palette rows.",
            developer_message=str(getattr(response, "data", response))
        )


    except Exception as e:
        return standard_response(
            status="INTERNAL_SERVER_ERROR",
            status_code=500,
            message="An unexpected error occurred during symptom prompt insert.",
            developer_message=str(e)
        )
    
@flashcards_bp.route("/score_contribution", methods=["POST"])
def submit_tone_pallet():


                insert_data.append({
                "tone": item["tone"],
                "used_for": item["used_for"],
                "pacing": item["pacing"],
                "language_style": item["language_style"],
                "vault_types": item["vault_types"],
                "avoid": item["avoid"]
                })
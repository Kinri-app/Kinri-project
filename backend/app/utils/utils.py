import json
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import supabase

load_dotenv()
# Questionnaire to get users weighted score per each condition using a likert_scale and ten questions then return top 3 in json format
def questionnaire():
    # This is used to create a direct path to the 'questions_weights.json' file
    base_dir = os.path.dirname(__file__)

    file_path = os.path.join(base_dir, 'questions_weights.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)


    likert_scale = {
        "never": 0,
        "rarely":1,
        "sometimes": 2,
        "often":3,
        "always": 4
    }

    assessment_score = {
        'cptsd': 0,
        'ptsd': 0,
        'gad': 0,
        'autism': 0,
        'depression': 0,
        'adhd': 0,
        'bpd': 0,
        'ocd': 0,
    }
    for question in questions[:10]:  # Only do first 10 questions
        print("\n" + question['question'])

        while True:
            user_input = input("Please type 'never', 'rarely', 'sometimes', 'often', or 'always': ").strip().lower()
            if user_input in likert_scale:
                break
            else:
                print("Invalid input. Try again.")

        score_value = likert_scale[user_input] / 4  # Normalize to 0.0 - 1.0
    # Using match and case to assign values to assesssment scores
        for condition, weight in question['conditions'].items():
            match condition.lower():
                case 'cptsd':
                    assessment_score['cptsd'] += score_value * weight
                case 'ptsd':
                    assessment_score['ptsd'] += score_value * weight
                case 'gad':
                    assessment_score['gad'] += score_value * weight
                case 'autism':
                    assessment_score['autism'] += score_value * weight
                case 'depression':
                    assessment_score['depression'] += score_value * weight
                case 'adhd':
                    assessment_score['adhd'] += score_value * weight
                case 'bpd':
                    assessment_score['bpd'] += score_value * weight
                case 'ocd':
                    assessment_score['ocd'] += score_value * weight
                case _:
                    print(f"Unknown condition: {condition}")


    top_3 = sorted(assessment_score.items(), key=lambda x: x[1], reverse=True)[:3]

    dict_list = [{'condtion': cond, 'score': score} for cond, score in top_3]

    top_3_json_convert = json.dumps(dict_list, indent=2)

    print(top_3_json_convert)
    return top_3_json_convert
    

def cosine_confidence(vec1, vec2) -> float:
    """Returns cosine similarity as a proxy confidence score between 0 and 1."""
    sim = cosine_similarity([vec1], [vec2])[0][0]
    return round((sim + 1) / 2, 4)  # Normalize from [-1,1] to [0,1]

def flatten_tags(card):
    return {
        "card_id": card["card_id"],
        "card_type": card["card_type"],
        "headline": card["headline"],
        "body": card["body"],
        "prompt": card["prompt"],
        "condition": card["tags"].get("condition", []),
        "emotion": card["tags"].get("emotion", []),
        "narrative_type": card["tags"].get("narrative_type", []),
        "usage_mode": card["tags"].get("usage_mode", [])
    }

def sync_user_to_db():
    user = g.current_user
    auth0_id = user.get("sub")
    email = user.get("email")
    name = user.get("name")
    picture = user.get("picture")

    existing = supabase.table("users").select("*").eq("auth0_id", auth0_id).single().execute()

    if existing.data:
        # The following compares and updates fields if needed
        updates = {}

        if existing.data.get("email") != email:
            updates["email"] = email
        if existing.data.get("name") != name:
            updates["name"] = name
        if existing.data.get("picture") != picture:
            updates["picture"] = picture

        if updates:
            supabase.table("users").update(updates).eq("auth0_id", auth0_id).execute()
            
        return

    # Insert new user
    supabase.table("users").insert({
        "id": auth0_id,
        "email": email,
        "name": name,
        "picture": picture
    }).execute()

    # app/utils/session_utils.py or inside the same file

def cleanup_old_sessions(user_id, max_sessions=10):
    res = supabase.table("session") \
        .select("id, vault_card_id, created_at") \
        .eq("user_id", user_id) \
        .order("created_at", desc=True) \
        .execute()

    all_sessions = res.data or []

    # Filter to those not tied to vault_card_id
    deletable_sessions = [
        s for s in all_sessions[max_sessions:] if not s.get("vault_card_id")
    ]

    ids_to_delete = [s["id"] for s in deletable_sessions]

    if ids_to_delete:
        supabase.table("session").delete().in_("id", ids_to_delete).execute()


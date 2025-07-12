from collections import defaultdict

def calculate_condition_scores(user_responses, question_weights):
    """
    Calculates weighted scores per condition based on user responses.
    """

    # Map question id to condition weights
    question_map = {str(q["id"]).lower(): q["conditions"] for q in question_weights}

    scores = defaultdict(float)

    for response in user_responses:
        qid = str(response["id"]).lower().lstrip("q")
        score = response["score"]

        if qid not in question_map:
            continue

        weights = question_map[qid]

        for condition, weight in weights.items():
            scores[condition.lower()] += (score / 4) * weight

    top_3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

    return [{"condtion": cond, "score": round(score, 3)} for cond, score in top_3]

def verify_researcher(profile):
    return {
        "researcher_id": profile["id"],
        "trust_score": profile["trust_score"],
        "verified": profile["trust_score"] >= 60
    }

def verify_profile(profile: dict):
    trust_score = profile.get("trust_score", 0)
    return {
        "verified": trust_score >= 60,
        "trust_score": trust_score,
        "escalation_required": trust_score < 60
    }

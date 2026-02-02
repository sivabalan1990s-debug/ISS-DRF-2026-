def compute_trust_score(publications, ethics_declared, artifacts_verified):
    score = 0
    score += len(publications) * 10
    score += 20 if ethics_declared else 0
    score += 30 if artifacts_verified else 0
    return min(score, 100)

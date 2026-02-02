import hashlib

def generate_researcher_id(name: str, affiliation: str) -> str:
    """
    Generates a non-reversible researcher fingerprint.
    No personal documents required.
    """
    raw = f"{name.lower()}::{affiliation.lower()}"
    return hashlib.sha256(raw.encode()).hexdigest()

import hashlib
from pathlib import Path

def hash_artifact(file_path: str) -> str:
    """
    Ensures research integrity.
    """
    content = Path(file_path).read_bytes()
    return hashlib.sha256(content).hexdigest()

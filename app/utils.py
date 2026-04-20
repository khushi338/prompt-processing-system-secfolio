import hashlib
import re


def normalize_prompt(prompt: str) -> str:
    """
    Normalize input prompt to improve cache hits.
    - Lowercase
    - Remove extra spaces
    - Strip special characters (basic)
    """
    prompt = prompt.lower()
    prompt = re.sub(r"\s+", " ", prompt)  # remove extra spaces
    prompt = prompt.strip()
    return prompt


def generate_cache_key(prompt: str) -> str:
    """
    Generate a consistent hashed key for Redis storage.
    Prevents issues with long or messy keys.
    """
    normalized = normalize_prompt(prompt)
    return hashlib.sha256(normalized.encode()).hexdigest()


def simple_similarity(prompt1: str, prompt2: str) -> float:
    """
    Basic similarity function (NOT true semantic).
    Used only for demonstration.

    Returns value between 0 and 1
    """
    set1 = set(normalize_prompt(prompt1).split())
    set2 = set(normalize_prompt(prompt2).split())

    if not set1 or not set2:
        return 0.0

    intersection = len(set1 & set2)
    union = len(set1 | set2)

    return intersection / union
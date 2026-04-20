import time
from app.cache import store_cache
from app.rate_limiter import allow_request

def mock_llm(prompt):
    time.sleep(1)  # simulate delay
    return f"Processed response for: {prompt}"

def process_job(prompt):
    # Rate limit handling
    while not allow_request():
        time.sleep(1)

    result = mock_llm(prompt)

    # Store in cache
    store_cache(prompt, result)

    return result
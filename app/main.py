from fastapi import FastAPI
from threading import Thread
import time

app = FastAPI()

# In-memory structures
queue = []
cache = {}

# Rate limiting config
rate_limit = {"count": 0, "time": time.time()}
LIMIT = 300
WINDOW = 60  # seconds


def worker():
    while True:
        if queue:
            prompt = queue.pop(0)

            # Rate limiting logic
            current_time = time.time()
            if current_time - rate_limit["time"] > WINDOW:
                rate_limit["count"] = 0
                rate_limit["time"] = current_time

            if rate_limit["count"] >= LIMIT:
                time.sleep(1)
                continue

            rate_limit["count"] += 1

            # Simulate LLM processing
            time.sleep(1)
            response = f"Processed: {prompt}"

            # Store in cache
            cache[prompt] = response

        else:
            time.sleep(0.5)


# Start worker thread
Thread(target=worker, daemon=True).start()


@app.get("/")
def home():
    return {"message": "Prompt Processing System Running 🚀"}


@app.post("/prompt")
def process_prompt(prompt: str):
    # Check cache first
    if prompt in cache:
        return {
            "status": "cached",
            "response": cache[prompt]
        }

    # Add to queue
    queue.append(prompt)

    return {
        "status": "queued",
        "message": "Your request is being processed asynchronously"
    }


@app.get("/status")
def status():
    return {
        "queue_length": len(queue),
        "cache_size": len(cache),
        "rate_limit_count": rate_limit["count"]
    }
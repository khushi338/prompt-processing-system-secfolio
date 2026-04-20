import time
from redis import Redis

redis_conn = Redis(host="localhost", port=6379)

LIMIT = 300
WINDOW = 60  # seconds

def allow_request():
    current_time = int(time.time())
    window = current_time // WINDOW

    key = f"rate_limit:{window}"

    count = redis_conn.incr(key)

    if count == 1:
        redis_conn.expire(key, WINDOW)

    return count <= LIMIT
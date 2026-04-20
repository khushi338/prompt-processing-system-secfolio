from redis import Redis

redis_conn = Redis(host="localhost", port=6379)

def check_cache(prompt):
    return redis_conn.get(prompt)

def store_cache(prompt, response):
    redis_conn.set(prompt, response)
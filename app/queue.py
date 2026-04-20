from rq import Queue
from redis import Redis
from app.worker import process_job

redis_conn = Redis(host="localhost", port=6379)
queue = Queue(connection=redis_conn)

def enqueue_prompt(prompt):
    job = queue.enqueue(process_job, prompt)
    return job.id
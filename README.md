# Prompt Processing System

## Overview
A scalable prompt processing system designed for high-throughput AI workloads.  
Implements asynchronous execution, caching, and rate limiting.

## Features
- Async processing using background worker
- Queue-based architecture
- In-memory caching (simulating semantic cache)
- Rate limiting (300 requests/minute)
- Fault-tolerant design (easily extendable to Redis)

## Architecture
Client → FastAPI → Queue → Worker → LLM (mock)
                             ↓
                          Cache

## API

### POST /prompt
Submit a prompt for processing.

## Example Flow
1. First request → queued  
2. Worker processes → stores in cache  
3. Second request → instant cached response  

## Tech Stack
- FastAPI
- Python threading (worker simulation)

## Note
Due to environment constraints, Redis is replaced with in-memory structures.  
Architecture is designed to be easily switched to Redis/RQ for production use.

## Future Improvements
- Redis + RQ integration
- Semantic search using embeddings
- Distributed workers
- Job status endpoint
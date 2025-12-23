# app.py
import os
import json
import random

import redis
from fastapi import FastAPI, Query

from main import binary_search

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
ARRAY_KEY = "numbers"

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

app = FastAPI(title="Binary Search Service")


def get_or_create_array():
    data = r.get(ARRAY_KEY)
    if data:
        return json.loads(data)

    arr = sorted(random.randint(0, 200) for _ in range(100))
    r.set(ARRAY_KEY, json.dumps(arr))
    return arr


@app.get("/search")
def search(target: int = Query(..., description="Искомое число")):
    """
    Пример запроса: GET /search?target=42
    Ответ: {"index": 10}
    """
    arr = get_or_create_array()
    idx = binary_search(arr, target)
    return {"index": idx}

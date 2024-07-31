import time

import redis
from fastapi import FastAPI

app = FastAPI()
data_base = redis.Redis(host="redis", port=6379)


def get_landing_visits():
    retries = 3
    while True:
        try:

            return data_base.incr("landing_visit")

        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(1)


@app.get("/")
async def root():
    visitors = get_landing_visits()
    return {"landing_visit": visitors}


# test

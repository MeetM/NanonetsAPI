import os
import redis
import json


def fetch_best_params(model_id):
    redis_url = os.environ['REDIS_URL']
    db = redis.StrictRedis(host=redis_url, port=6379, db=0)
    res = db.get("BEST_PARAMS_"+str(model_id))
    return json.loads(res)

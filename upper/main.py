from flask import Flask, jsonify
import redis

app = Flask(__name__)

VERSION = "2.0"
REDIS_SERVICE_NAME = "redis-leader"
REDIS_SERVICE_PORT = 6379


@app.get("/<req_str>")
def get_upper(req_str: str):
    r = redis.Redis(host=REDIS_SERVICE_NAME, port=REDIS_SERVICE_PORT)
    # How many times (including this one) was this string requested?
    count = r.incrby(req_str, 1)

    if count <= 5:
        res = {"version": VERSION, "upper": req_str.upper()}
        return jsonify(res)

    error = "Too many requests."

    return jsonify({"version": VERSION, "error": error})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

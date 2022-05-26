import logging

from flask import Flask, request
import hazelcast

app = Flask(__name__)
host = "localhost"
number_copy = 1  # 1, 2 or 3
port = 9001 + number_copy

logging.basicConfig(level=logging.INFO)

hz_cluster = hazelcast.HazelcastClient(
    cluster_members=["127.0.0.1:570" + str(number_copy)])

hz_map = hz_cluster.get_map("logging-map").blocking()


@app.post("/logging")
def post_request():
    uuid = str(request.form["uuid"])
    message = request.form["msg"]

    hz_map.lock(uuid)
    try:
        hz_map.put(uuid, message)
    finally:
        hz_map.unlock(uuid)

    print("message '" + message + "' received")
    return ""


@app.get("/logging")
def get_request():
    return ", ".join(hz_map.values())


if __name__ == "__main__":
    app.run(host, port)

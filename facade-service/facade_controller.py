from flask import Flask, request
import hazelcast
import logging
import requests
import uuid
import random


app = Flask(__name__)
host = "localhost"
port = 9000

log_serv = ["http://" + host + ":901" + str(i) + "/logging" for i in range(1, 4)]
mes_serv = ["http://" + host + ":902" + str(i) + "/message" for i in range(1, 3)]

logging.basicConfig(level=logging.INFO)

hz_cluster = hazelcast.HazelcastClient(
    cluster_members=["127.0.0.1:5701",
                     "127.0.0.1:5702",
                     "127.0.0.1:5703"])

hz_queue = hz_cluster.get_queue("messaging-queue").blocking()


@app.post("/facade")
def post_request():
    # logging service
    response = requests.post(random.choice(log_serv), data={"uuid": uuid.uuid4(), "msg": request.get_json()})
    # message service
    hz_queue.put(str(request.get_json()))
    return response.text


@app.get("/facade")
def get_request():
    logging_response = requests.get(random.choice(log_serv))
    message_response = requests.get(random.choice(mes_serv))
    return "Logging Service response: " + logging_response.text + \
           "\nMessage Service response: " + message_response.text


if __name__ == "__main__":
    app.run(host, port)

from flask import Flask, request
import requests
import uuid
import random

import hazelcast

app = Flask(__name__)
host = "localhost"
port = 9000

mes_serv = "http://" + host + ":9001/message"
log_serv = ["http://" + host + ":900" + str(i) + "/logging" for i in range(2, 5)]


@app.post("/facade")
def post_request():
    response = requests.post(random.choice(log_serv), data={"uuid": uuid.uuid4(), "msg": request.get_json()})
    return response.text


@app.get("/facade")
def get_request():
    logging_response = requests.get(random.choice(log_serv))
    message_response = requests.get(mes_serv)
    return "Logging Service response: " + logging_response.text + \
           "\nMessage Service response: " + message_response.text


if __name__ == "__main__":
    app.run(host, port)

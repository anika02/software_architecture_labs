from flask import Flask, request
import requests
import uuid

app = Flask(__name__)
host = "localhost"
port = 8080

logging_service = "http://" + host + ":8081/logging"
message_service = "http://" + host + ":8082/message"


@app.post("/facade")
def post_request():
    response = requests.post(logging_service, data={"uuid": uuid.uuid4(), "msg": request.get_json()})
    return response.text


@app.get("/facade")
def get_request():
    logging_response = requests.get(logging_service)
    message_response = requests.get(message_service)
    return "Logging Service response: " + logging_response.text + \
           "\nMessage Service response: " + message_response.text


if __name__ == "__main__":
    app.run(host, port)

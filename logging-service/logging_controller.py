from flask import Flask, request

app = Flask(__name__)
host = "localhost"
port = 8081

storage = dict()


@app.post("/logging")
def post_request():
    uuid = request.form["uuid"]
    message = request.form["msg"]
    storage[uuid] = message
    print("uuid: ", uuid, "\nmessage: ", message)
    return


@app.get("/logging")
def get_request():
    return ", ".join(storage.values())


if __name__ == "__main__":
    app.run(host, port)

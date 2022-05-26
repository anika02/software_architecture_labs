from flask import Flask

app = Flask(__name__)
host = "localhost"
port = 9001


@app.get("/message")
def message():
    return "not implemented yet"


if __name__ == "__main__":
    app.run(host, port)

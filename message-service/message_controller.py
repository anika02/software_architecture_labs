from flask import Flask
import hazelcast
import logging

app = Flask(__name__)
host = "localhost"
number_copy = 1  # 1, 2
port = 9020 + number_copy

logging.basicConfig(level=logging.INFO)

hz_cluster = hazelcast.HazelcastClient(
    cluster_members=["127.0.0.1:5701",
                     "127.0.0.1:5702",
                     "127.0.0.1:5703"])

hz_queue = hz_cluster.get_queue("messaging-queue").blocking()

storage = []


@app.get("/message")
def message():
    while not hz_queue.is_empty():
        item = hz_queue.take()
        print("Consumed: " + str(item))
        storage.append(item)
    print("Consumer Finished!")
    return ", ".join(storage)


if __name__ == "__main__":
    app.run(host, port)

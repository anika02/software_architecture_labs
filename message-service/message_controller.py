from flask import Flask
import hazelcast
import logging
import consul
import uuid

host_name = "localhost"
consul_port = 8500
service_port = 9021  # 9020 or 9021
service_name = "message-service"

service_consul = consul.Consul(host=host_name, port=consul_port)
service_consul.agent.service.register(name=service_name, port=service_port,
                                      service_id=f'{service_name}:{uuid.uuid4()}')

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

hz_cluster = hazelcast.HazelcastClient(
    cluster_members=service_consul.kv.get("hazelcast")[1]["Value"].decode("utf-8").split())

hz_queue = hz_cluster.get_queue(service_consul.kv.get("hz_queue")[1]["Value"].decode("utf-8")).blocking()

storage = []
print("Message service registered!")


@app.get("/message")
def get_request():
    while not hz_queue.is_empty():
        item = hz_queue.take()
        print("Consumed: " + str(item))
        storage.append(item)
    print("Consumer Finished!")
    return ", ".join(storage)


if __name__ == "__main__":
    app.run(host_name, service_port)

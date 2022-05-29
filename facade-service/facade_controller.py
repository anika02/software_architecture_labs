from flask import Flask, request
import hazelcast
import logging
import consul
import uuid
import requests
import random

host_name = "localhost"
consul_port = 8500
service_port = 9000
service_name = "facade-service"

service_consul = consul.Consul(host=host_name, port=consul_port)
service_consul.agent.service.register(name=service_name, port=service_port,
                                      service_id=f'{service_name}:{uuid.uuid4()}')

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

hz_cluster = hazelcast.HazelcastClient(
    cluster_members=service_consul.kv.get("hazelcast")[1]["Value"].decode("utf-8").split())

hz_queue = hz_cluster.get_queue(service_consul.kv.get("hz_queue")[1]["Value"].decode("utf-8")).blocking()
print("Facade service registered!")


def get_random_port(name):
    print([value['Port'] for value in service_consul.agent.services().values() if value["Service"] == name + "-service"])
    return "http://localhost:" + str(random.choice(
        [value['Port'] for value in service_consul.agent.services().values() if value["Service"] == name + "-service"])) + f'/{name}'


@app.post("/facade")
def post_request():
    # logging service
    response = requests.post(get_random_port("logging"), data={"uuid": uuid.uuid4(), "msg": request.get_json()})
    # message service
    hz_queue.put(str(request.get_json()))
    return response.text


@app.get("/facade")
def get_request():
    logging_response = requests.get(get_random_port("logging"))
    message_response = requests.get(get_random_port("message"))
    return "Logging Service response: " + logging_response.text + \
           "\nMessage Service response: " + message_response.text


if __name__ == "__main__":
    app.run(host_name, service_port)

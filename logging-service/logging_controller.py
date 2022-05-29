from flask import Flask, request
import hazelcast
import logging
import consul
import uuid

host_name = "localhost"
consul_port = 8500
service_port = 9010  # 9010, 9011 or 9012
service_name = "logging-service"

service_consul = consul.Consul(host=host_name, port=consul_port)
service_consul.agent.service.register(name=service_name, port=service_port,
                                      service_id=f'{service_name}:{uuid.uuid4()}')

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

hz_cluster = hazelcast.HazelcastClient(
    cluster_members=service_consul.kv.get("hazelcast")[1]["Value"].decode("utf-8").split())

hz_map = hz_cluster.get_map(service_consul.kv.get("hz_map")[1]["Value"].decode("utf-8")).blocking()
print("Logging service registered!")


@app.post("/logging")
def post_request():
    mes_id = str(request.form["uuid"])
    message = request.form["msg"]

    hz_map.lock(mes_id)
    try:
        hz_map.put(mes_id, message)
    finally:
        hz_map.unlock(mes_id)

    print("message '" + message + "' received")
    return ""


@app.get("/logging")
def get_request():
    return ", ".join(hz_map.values())


if __name__ == "__main__":
    app.run(host_name, service_port)

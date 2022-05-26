import hazelcast
import logging

logging.basicConfig(level=logging.INFO)

hz_cluster = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=["127.0.0.1:5701",
                     "127.0.0.1:5702",
                     "127.0.0.1:5703"])


hz_map = hz_cluster.get_map("distributed-map").blocking()

for i in range(1000):
    hz_map.lock(i)
    hz_map.set(i, "value_" + str(i))

hz_cluster.shutdown()

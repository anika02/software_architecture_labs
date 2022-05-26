import time

import hazelcast
import logging

logging.basicConfig(level=logging.INFO)


class PessimisticUpdateMember:
    def __init__(self):
        hz_cluster = hazelcast.HazelcastClient(
            cluster_name="dev",
            cluster_members=["127.0.0.1:5701",
                             "127.0.0.1:5702",
                             "127.0.0.1:5703"])

        hz_map = hz_cluster.get_map("distributed-map").blocking()

        key = "1"
        hz_map.put(key, "0")
        print("Starting")
        for _ in range(1000):
            hz_map.lock(key)
            try:
                value = hz_map.get(key)
                time.sleep(1)
                value = str(int(value) + 1)
                hz_map.put(key, value)
            finally:
                hz_map.unlock(key)
        print("Finished! Result = " + hz_map.get(key))
        hz_cluster.shutdown()


pessimistic = PessimisticUpdateMember()

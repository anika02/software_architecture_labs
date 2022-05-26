import time

import hazelcast
import logging

logging.basicConfig(level=logging.INFO)


class RacyUpdateMember:
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
            value = hz_map.get(key)
            time.sleep(0.1)
            value = str(int(value) + 1)
            hz_map.put(key, value)
        print("Finished! Result = " + hz_map.get(key))
        hz_cluster.shutdown()


pessimistic = RacyUpdateMember()

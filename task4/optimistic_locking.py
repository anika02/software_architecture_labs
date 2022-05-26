import time

import hazelcast
import logging

from hazelcast.serialization.api import StreamSerializer

logging.basicConfig(level=logging.INFO)


class Value(StreamSerializer):
    def __init__(self, other=None):
        if other is not None:
            self.amount = other.amount
        else:
            self.amount = 0

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Value):
            return False
        return other.amount == self.amount


class OptimisticMember:
    def __init__(self):
        hz_cluster = hazelcast.HazelcastClient(
            cluster_name="dev",
            cluster_members=["127.0.0.1:5701",
                             "127.0.0.1:5702",
                             "127.0.0.1:5703"])

        hz_map = hz_cluster.get_map("distributed-map").blocking()

        key = "1"
        hz_map.put(key, Value())
        print("Starting")
        for _ in range(1000):
            while True:
                old_value = hz_map.get(key)
                new_value = Value(old_value)
                time.sleep(1)
                new_value.amount += 1
                if hz_map.replace_if_same(key, old_value, new_value):
                    break
        print("Finished! Result = " + hz_map.get(key).amount)
        hz_cluster.shutdown()


pessimistic = OptimisticMember()

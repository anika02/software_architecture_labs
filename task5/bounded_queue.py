import hazelcast
import logging
import time

logging.basicConfig(level=logging.INFO)


class ProducerMember:
    def __init__(self):
        hz_cluster = hazelcast.HazelcastClient(
            cluster_name="dev",
            cluster_members=["127.0.0.1:5701",
                             "127.0.0.1:5702",
                             "127.0.0.1:5703"])
        queue = hz_cluster.get_queue("distributed-queue").blocking()
        for k in range(1, 100):
            queue.put(k)
            print("Producing: " + str(k))
            time.sleep(1)
        queue.put(-1)
        print("Producer Finished!")
        hz_cluster.shutdown()


class ConsumerMember:
    def __init__(self):
        hz_cluster = hazelcast.HazelcastClient(
            cluster_name="dev",
            cluster_members=["127.0.0.1:5701",
                             "127.0.0.1:5702",
                             "127.0.0.1:5703"])
        queue = hz_cluster.get_queue("distributed-queue").blocking()
        while True:
            item = queue.take()
            print("Consumed: " + str(item))
            if item == -1:
                queue.put(-1)
                break
            time.sleep(1)
        print("Consumer Finished!")
        hz_cluster.shutdown()


writer = ProducerMember()
# reader = ConsumerMember()

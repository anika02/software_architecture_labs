import consul

service_consul = consul.Consul()
service_consul.kv.put("hazelcast", "127.0.0.1:5701 127.0.0.1:5702 127.0.0.1:5703")
service_consul.kv.put("hz_map", "logging-map")
service_consul.kv.put("hz_queue", "message-queue")

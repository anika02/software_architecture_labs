# Microservices with Hazelcast Distributed Map

### Architecture
![image](https://user-images.githubusercontent.com/60771374/170538654-9d4c1514-0bb9-436f-885c-3705d4731e2c.png)

Runned logging service copies on the different ports. Each service has a separate node in Hazelcast Distributed Map.

### 10 POST requests
Requests are in the file **POST_requests.http**

##### all POST requests
![image](https://user-images.githubusercontent.com/60771374/170539017-70c05506-9978-4beb-88ea-bd9096520f9f.png)

##### logging service copy 1
```
localhost port: 9002
hazelcast: 127.0.0.1:5701
```
![image](https://user-images.githubusercontent.com/60771374/170539620-cf0aa963-fccb-407e-a38c-88020fe1c03a.png)


##### logging service copy 2
```
localhost port: 9003
hazelcast: 127.0.0.1:5702
```
![image](https://user-images.githubusercontent.com/60771374/170539651-305251d0-6b56-444c-ab41-8173ec21d936.png)


##### logging service copy 3
```
localhost port: 9004
hazelcast: 127.0.0.1:5703
```
![image](https://user-images.githubusercontent.com/60771374/170539702-c1b1d9e0-17e8-4c9f-9993-2c71d3260d6b.png)

### GET request
Request are in the file **GET_requests.http**
![image](https://user-images.githubusercontent.com/60771374/170539970-f2f1fc39-ca50-4486-81f8-b7bfdca9ddb6.png)

### Close one of three logging service copies
Since we have directly specified in the code a random choice between the three service copies, GET and POST requests will randomly choose one of the copies, and each time we access the disabled service, an error will be returned.
Also, due to the fact that the nodes are tied to a certain copy of the service, the node that is tied to the disabled service will stop to function. Writing and reading to the map will take place only from the included nodes (in other words, further filling of the distributed map with data will take place only on these two nodes). And all data with work services will be returned.
Important: my code is on python and hazelcast node does not turn off when one of copies is turned off.
##### GET request to working service
![image](https://user-images.githubusercontent.com/60771374/170542833-5aaae5aa-dceb-498c-aa1d-1070bbbdcab0.png)
##### GET request to disabled service
![image](https://user-images.githubusercontent.com/60771374/170542863-6d93fef1-31d3-4c84-95b2-e602365df0da.png)



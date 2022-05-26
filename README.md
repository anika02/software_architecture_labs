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

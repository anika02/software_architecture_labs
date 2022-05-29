# Microservices with Messaging queue

### Architecture
![image](https://user-images.githubusercontent.com/60771374/170884165-6e4358fb-dce0-4aac-a64f-09ea714a1444.png)


### 10 POST requests
Requests are in the file **POST_requests.http**
![image](https://user-images.githubusercontent.com/60771374/170884643-ca4ab4de-6256-4df7-bb5b-2875ba698ce3.png)


### Results for logging services
##### logging service copy 1
![image](https://user-images.githubusercontent.com/60771374/170884650-90b41389-bc35-441d-b01d-be1091166ed9.png)

##### logging service copy 2
![image](https://user-images.githubusercontent.com/60771374/170884655-c4abae01-2dfe-498a-b985-b618b21b0a2c.png)

##### logging service copy 3
![image](https://user-images.githubusercontent.com/60771374/170884663-f4da4e18-d3b9-497f-96c5-d41b3e28e6b0.png)

### GET request
Request are in the file **GET_requests.http**

#### GET #1
![image](https://user-images.githubusercontent.com/60771374/170884672-fa6ea9e1-5621-4c76-b01a-07088fa5ec9f.png)
**messages service copy 2**
![image](https://user-images.githubusercontent.com/60771374/170884698-d0e63f6e-3133-4379-8e31-3ef6df3d80b6.png)

#### GET #2
![image](https://user-images.githubusercontent.com/60771374/170884707-de827e8b-0b9c-40a4-855c-afcbf0af9eeb.png)
**messages service copy 1**
![image](https://user-images.githubusercontent.com/60771374/170884712-0732fe57-8b99-4f7b-b7a4-e0db946bca94.png)

#### GET #3
![image](https://user-images.githubusercontent.com/60771374/170884714-7d554ea3-c2fd-4752-842f-5ade244b3b8d.png)
**messages service copy 1**
![image](https://user-images.githubusercontent.com/60771374/170884720-7056ccaf-b59a-40d3-8d78-bd1ad86ed143.png)

Conclusions of GET requests:
1. Messages received from the logging service stored in the Hazelcast Distributed Map are randomly ordered. Messages received from the messages service are sorted in the order of our POST requests (since messages are received from the Messaging queue, they are added in the same order to the message service storage, which is a Python list).
2. After making several GET requests, you can see that messages from the message service will be returned as different lists. This is because each copy of the messages service has its own storage, and when we do a GET request, we will get back the data from the storage of the service that was randomly selected by the facade service. The storage itself is replenished only during GET requests, and all data from the Messaging queue will be stored in the storage of the corresponding selected messages service.

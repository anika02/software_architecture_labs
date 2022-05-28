# Microservices with Messaging queue

### Architecture
![image](https://user-images.githubusercontent.com/60771374/170826448-b43b19d2-a4ea-4986-88e8-fe61fd0fb232.png)

### 10 POST requests
Requests are in the file **POST_requests.http**
![image](https://user-images.githubusercontent.com/60771374/170826796-8da94ed6-8a7d-4309-825b-d94b307fbd12.png)

### Results for logging services
##### logging service copy 1
![image](https://user-images.githubusercontent.com/60771374/170826857-34341727-1c74-4a36-82f0-4dd07c157490.png)

##### logging service copy 2
![image](https://user-images.githubusercontent.com/60771374/170826869-488f8a1d-1f27-4702-b75d-d0d626ac9974.png)

##### logging service copy 3
![image](https://user-images.githubusercontent.com/60771374/170826862-7f812ee1-07ed-4ccf-a6c0-a8aa85d17946.png)

### Some GET requests
#### GET #1
![image](https://user-images.githubusercontent.com/60771374/170826906-cdd2146e-0e61-4fc2-bb2d-acb5f427ad4d.png)
**messages service copy 1**
![image](https://user-images.githubusercontent.com/60771374/170826911-edb51148-7c56-43e2-92f3-b924b0620c5e.png)

#### GET #2
![image](https://user-images.githubusercontent.com/60771374/170826932-841a1c18-5727-4f1b-b974-111a6baf0498.png)
**messages service copy 1**
![image](https://user-images.githubusercontent.com/60771374/170826941-f23be480-1cbc-4aec-8a32-31f4916e16d0.png)

#### GET #5
![image](https://user-images.githubusercontent.com/60771374/170826963-e8919fd4-4dac-4b48-bf5b-990db8f5de72.png)
**messages service copy 2**
![image](https://user-images.githubusercontent.com/60771374/170826975-6a5f6ca7-6bcb-4ac2-85a7-f25293e5ef54.png)

Conclusions of GET requests:
1. Messages received from the logging service stored in the Hazelcast Distributed Map are randomly ordered. Messages received from the messages service are sorted in the order of our POST requests (since messages are received from the Messaging queue, they are added in the same order to the message service storage, which is a Python list).
2. After making several GET requests, you can see that messages from the message service will be returned as different lists. This is because each copy of the messages service has its own storage, and when we do a GET request, we will get back the data from the storage of the service that was randomly selected by the facade service. The storage itself is replenished only during GET requests, and all data from the Messaging queue will be stored in the storage of the corresponding selected messages service.

# Microservices with Messaging queue

### Architecture
![image](https://user-images.githubusercontent.com/60771374/170884165-6e4358fb-dce0-4aac-a64f-09ea714a1444.png)

### Run
```
1. hazelcast --- hazelcast-5.1.1/bin/hz-start.bat
2. consul --- consul agent -dev
3. run_consul.py
4. 1 instance of facade
5. 3 inctances of logging service with different service_port
6. 2 inctances of messaging service with different service_port
```
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
![image](https://user-images.githubusercontent.com/60771374/170884761-be4194b9-b63d-4f99-8f77-c3a16bc2d6c4.png)

As we can see, we got a similar result to work without a Consul. But, thanks to the Consul, we no longer had to register every address, and now we can safely add new services and turn off non-working ones. In addition, in communication with the Consul, he will return us the addresses of only work services.

# Basic architecture of microservices
### Architecture
![image](https://user-images.githubusercontent.com/60771374/170472138-daaf6f1a-a49f-44f2-8574-5c3e73ffa9e6.png)

### Usage
You can use file **Requests.http** to do POST and GET requests to services

### POST and GET requests
The photos show the request order numbers that matches the requests in **Requests.http**
![image](https://user-images.githubusercontent.com/60771374/170474664-dc1d3d20-7029-41b9-9953-2bca5d0027e9.png)
![image](https://user-images.githubusercontent.com/60771374/170474701-0cfc0afa-5d5f-4329-8ba3-98ca025b26be.png)
![image](https://user-images.githubusercontent.com/60771374/170474730-c92102bd-5e48-4f53-98cd-09a252d0cbcd.png)

```
3 - first GET request when we have one message in logging service storage
5 - one of POST request (message _msg3_)
6 - GET request when we have three messages in logging service storage
```
In the third photo we are lucky with the order of messages, because usually the order is not saved and it is necessary to add some functionality to organize messages.

### Microservice console
##### facade service
![image](https://user-images.githubusercontent.com/60771374/170475488-1fad584c-5052-4f67-a814-e2e7a81b7b26.png)

##### logging service
![image](https://user-images.githubusercontent.com/60771374/170475591-d9a23eb6-b980-48f8-bcb2-2c32d2d9472b.png)
Here, in addition to basic information, the content of the received message is displayed.

##### message service
![image](https://user-images.githubusercontent.com/60771374/170475551-c3fe960b-e15b-4a7c-aa8a-27b523f6b2a9.png)

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

# Distributed Map

### Task 3
#### 3 nodes work
![image](https://user-images.githubusercontent.com/60771374/170478716-f10a4455-bdcb-4a32-99bc-e364b5ab040c.png)
The distribution of values by nodes in the distributed map is more or less uniform (339, 318, 343).

#### 2 nodes work (after 1 node deleting)
![image](https://user-images.githubusercontent.com/60771374/170478742-222de1c5-b085-443c-8cb2-76c1ec0f150a.png)
All elements are more or less evenly distributed between the two remaining nodes (522, 438).

### Task 4
RacyUpdateMember is not safe, when is run by more than one cluster member simultaneously. And OptimisticMember or PessimisticUpdateMember can solve this problem. OptimisticMember has increased productivity compared to PessimisticUpdateMember. In turn, PessimisticUpdateMember is more reliable than OptimisticMember in terms of data consistency.

Some photos from the running these methods: 

RacyUpdateMember (without locking)
![image](https://user-images.githubusercontent.com/60771374/170490849-d0eebd01-36a9-4f32-8f7d-9d08e15b161a.png)

PessimisticUpdateMember (pessimistic locking)
![image](https://user-images.githubusercontent.com/60771374/170490956-25a1a1c7-0bd8-411a-8e78-b78e5da1a80c.png) ![image](https://user-images.githubusercontent.com/60771374/170491046-af807e2a-c9f1-4ed0-bec1-108918bf5c96.png) ![image](https://user-images.githubusercontent.com/60771374/170491096-969905ae-7f20-40de-bbd5-31feba079bb2.png)

OptimisticMember (optimistic locking)
![image](https://user-images.githubusercontent.com/60771374/170491192-28047ee5-0812-45ec-b02a-2625bcf06427.png) ![image](https://user-images.githubusercontent.com/60771374/170491252-242d818d-a268-435c-a548-069c609a8f87.png) ![image](https://user-images.githubusercontent.com/60771374/170491303-dfb3f5cc-ddb4-47f8-aa2a-717ef5956e9e.png) ![image](https://user-images.githubusercontent.com/60771374/170491330-60c3cc80-ab23-48fb-a14f-517c7d9ee3da.png)

### Task 5

##### Adding elements tp queue
![image](https://user-images.githubusercontent.com/60771374/170500827-a3213592-d484-42b8-989a-073dd41deb5a.png)
![image](https://user-images.githubusercontent.com/60771374/170501443-9d7b91d5-26c4-4e27-8940-1d7728bdec4c.png)


##### Taking elements
![image](https://user-images.githubusercontent.com/60771374/170500920-4aabf7fb-b8fa-43e2-831e-250f2bd5f259.png)
![image](https://user-images.githubusercontent.com/60771374/170501327-44b14228-dfbe-4392-9a60-8100e7863175.png)
![image](https://user-images.githubusercontent.com/60771374/170501183-a63f3307-2fd7-4690-ae44-aec079240086.png)

Adding elements to the filled queue that has not listeners: an error will occur and the queue will have the first elements.
Listeners will read while queue has data. If the data runs out (no producer or the producer writes slower than the data is read), listeners will be blocked.

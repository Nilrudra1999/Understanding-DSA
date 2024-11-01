# Intro to Double Ended Queues

Double ended Queues are an alternative implementation of the Queue class which allows for insertion and deletion of data from both ends of the Queue. All operations performed by this ADT class needs to be O(1) time thus, using singly linked lists is not efficient when implementing this ADT class since popping back requires O(n) runtime.

Even though this ADT class dosen't provide random access to it's elements it also doesn't have an particular FIFO or FILO behavior. The following are the implementation details of a typical Dequeue class:

![dequeue01](https://github.com/user-attachments/assets/b3f2cfae-6783-43eb-b64e-3b49b7530914)

Data members:
- List of default/given size (or LL)
- capacity
- size/used up space
- front
- back

Operations:
- init function (default constructor)
- various getter functions for the data members
- push_front() (front-1) % cap
- push_back() (back+1) % cap
- pop_front() (front+1) % cap
- pop_back() (back-1) % cap
- front() a getter function to get front's value
- back() a getter function to get back's value

![dequeue02](https://github.com/user-attachments/assets/e1d27661-b4b6-4fb0-b416-fa9bfa7a1fee)

![dequeue03](https://github.com/user-attachments/assets/9574452e-ba8c-472a-ad26-bf086601d398)

![dequeue04](https://github.com/user-attachments/assets/8b8daafd-23c3-4a6c-8210-1a9b5ae796f8)

![dequeue05](https://github.com/user-attachments/assets/de7c5a67-001c-4a42-b5b3-fd6c98d19513)

![dequeue06](https://github.com/user-attachments/assets/60c15e17-9b2f-4778-b0b3-d4a8105d4870)

![dequeue07](https://github.com/user-attachments/assets/58922a17-bcee-4a75-878e-b694b914d0d3)

![dequeue08](https://github.com/user-attachments/assets/b5571d93-938b-4ff4-afbc-956f0491263f)

Both the push front and back operations of this ADT class has O(1) runtimes.<br>
However when resizing, these functions have a O(n) runtime, except when implemented with a Doubly LL underlying data structure.

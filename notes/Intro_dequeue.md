# Intro to Double Ended Queues

Double ended Queues are an alternative implementation of the Queue class which allows for insertion and deletion of data from both ends of the Queue. All operations performed by this ADT class needs to be O(1) time thus, using singly linked lists is not efficient when implementing this ADT class since popping back requires O(n) runtime.

Even though this ADT class dosen't provide random access to it's elements it also doesn't have an particular FIFO or FILO behavior. The following are the implementation details of a typical Dequeue class:

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

Both the push front and back operations of this ADT class has O(1) runtimes.<br>
However when resizing, these functions have a O(n) runtime, except when implemented with a Doubly LL underlying data structure.
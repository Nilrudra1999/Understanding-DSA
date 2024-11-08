# Notes on LIST Abstract Data Types

These notes will explore the following:
- ✅ What is a LIST ADT?
- ✅ What are some implementations of LIST ADTs?
- What does the code look like?
- When should LISTs be used?
- Why should LISTs be used over other Data Structures?
- How are some LIST data structures the same?
- How are they different?

## What Are Some LIST ADTs?

### First defining what an Abstract Data Type is:

An Abstract Data Type, is the concept of a way of storing information inside a computer without the implementation details. It defines which operations this storage can perform and what sort of behavior the storage will have without specifying what the code will look.

### Second defining what a Data Structure is:

A Data structure, is when an ADT is take and implemented throughly with working code. Data structures are the implementation detail dependent versions of Abstract Data Types, its when the idea of the storage actually becomes real and specific to it's unique implementation.

### Then what is a LIST ADT?

LIST ADTs can be defined as the following:
1. A collection of data, thats related and/or has the same type
2. The data is ordered, theres a 1st, 2nd, ... nth index
3. Allows insertion operations (into the nth position)
4. Allows Searching operations (bi-directionally)
5. Allows Modifying operations (at the nth position)
6. Allows Removal operations (from the nth position)

## Implementations of LIST ADTs - Data Structures

Implementations of list Data Structures which follow the definition closely are:<br>
Arrays (contains C++ vectors & Python lists)<br>
Linked Lists (contains Singly, doubly, & Sentinal LL)<br>

Implementations of list Data Structures that impose their own behavior are:<br>
Stack (FILO)<br>
Queue (FIFO)<br>
Deque (Double ended Queue)<br>

These can be defined as "LIST Like" in nature.<br>
In the same way that a C++ vector is C array like.<br>

### Arrays

A collection of contiguous elements in memory, ordered by their index, that alway starts at i = 0.<br>

![array_dia](https://github.com/user-attachments/assets/dceb5046-a848-4080-a0a6-4e41f360af55)

### Linked List

A collection of nodes linked by pointers to form a chain like structure of all related data.<br>
Its nodes can be scattered throughout memory so long as they're connected by pointers, they're linked.<br>
The data structure always has a front and back pointer pointing to the front and back nodes.<br>
But depending on SLL or DLL, the nodes themselves may contain a prev pointer or not.<br>
Additionally, sentinal LL have nodes which gaurd the front and back positions in the list.<br>

![LL_dia](https://github.com/user-attachments/assets/45926111-81c2-4476-ba45-d4978c99fea7)

### Stack

The collection enforces a First-In-Last-Out behavior, only inserting and removing from one side.<br>

### Queue

The collection enforces a First-In-First-Out behavior, inserting only from one sides.<br>
However, removing can also only be done from one side but it must be the opposite side from inserting.<br>

### Dequeue

The collection enforces a double ended Queue nature, where insertion and removal happens on both sides.<br>
Both sides of the Dequeue act like Queues.<br>
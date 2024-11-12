# Notes on LIST Abstract Data Types

These notes will explore the following:
- ✅ What is a LIST ADT?
- ✅ What are some implementations of LIST ADTs?
- ✅ What does the code look like?
- ✅ When should LISTs be used?
- ✅ Why should LISTs be used over other Data Structures?

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

![stack_dia](https://github.com/user-attachments/assets/41ab6437-379c-446a-8e71-01dfaab2153a)

### Queue

The collection enforces a First-In-First-Out behavior, inserting only from one sides.<br>
However, removing can also only be done from one side but it must be the opposite side from inserting.<br>

![queue_dia](https://github.com/user-attachments/assets/49fc08af-90eb-4e30-9259-292e6647d08e)

### Dequeue

The collection enforces a double ended Queue nature, where insertion and removal happens on both sides.<br>
Both sides of the Dequeue act like Queues.<br>

![deqeue_dia](https://github.com/user-attachments/assets/17ec934f-802a-477e-bb7a-73e062bebcc1)

## Code for Array - Class

```python
class Array:
    def __init__(self, cap = 10):
        self.arr = [None] * cap
        self.cap = cap
        self.size = 0

    def get_cap(self):
        return self.cap

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    # Can either insert new data or modify existing data
    # O(1) when no resizing O(n) when resizing
    def push(self, value, i):
        if i >= self.cap and self.size != self.cap:
            raise IndexError('There is still space in the array, try [i] < capacity')
        elif i >= self.cap and self.size == self.cap:
            tmp_arr = self.arr
            self.cap *= 2
            self.arr = [None] * self.cap
            for i in range(self.size):
                self.arr[i] = tmp_arr[i]
            self.arr[i] = value
        else:
            self.arr[i] = value
        self.size += 1

    # Deletion operation runs at O(1) time
    def pop(self, i):
        if i >= self.cap:
            raise IndexError('Outside the range of the array, try [i] < capacity')
        elif i < self.cap and self.arr[i] == None:
            print('Index is already empty')
            return -1
        else:
            rc = self.arr[i]
            self.arr[i] = None
            self.size -= 1
            return rc

    # Binary search algorithm search O(log n) time
    def search(self, value):
        low = 0
        high = self.cap - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == value:
                return mid
            elif self.arr[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
        return -1
```

## Code for Linked List - Class

```python
class LinkedList:   # Doubly Linked List (unsorted)
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    class Node:     # Nodes of the Linked List
        def __init__(self, data, next = None, prev = None):
            self.data = data
            self.nx = next
            self.pr = prev
        
        def get_data(self):
            return self.data
        
        def get_next(self):
            return self.nx
        
        def get_prev(self):
            return self.pr
        
    def get_front(self):
        return self.front
    
    def get_back(self):
        return self.back
    
    def is_empty(self):
        return self.front == None and self.back == None
    
    # Inserts at the end of the Linked List always O(1) time
    def insert(self, data):
        nn = self.Node(data)
        if self.is_empty():
            self.front = nn
            self.back = nn
            self.size += 1
            return nn
        else:
            curr = self.back
            curr.nx = nn
            nn.pr = curr
            self.back = nn
            self.size += 1
            return nn
    
    # Deletes data from a valid point in the LL O(1) time
    def remove(self, node):
        if node == None:
            raise ValueError('Cannot remove a NULL pointer')
        if node == self.front:
            self.front = node.nx
            if self.front:
                self.front.pr = None
            else:
                self.back = None
        elif node == self.back:
            self.back = node.pr
            self.back.nx = None
        elif node.pr and node.nx:
            node.pr.nx = node.nx
            node.nx.pr = node.pr
        self.size -= 1

    # Uses LL traversal algorithm to search for the data O(n) time
    def search(self, value):
        curr = self.front
        while curr:
            if curr.get_data() == value:
                return curr
            curr = curr.nx
        return -1
```

## Code for Stack - Class

```python
class Stack:
    def __init__(self, cap = 10):
        self.stack = [None]*cap
        self.cap = cap
        self.size = 0
    
    def capacity(self):
        return self.cap
    
    def get_top(self):
        if self.is_empty():
            return None
        return self.stack[self.size - 1]
    
    def is_empty(self):
        return self.size == 0

    # Insertion operation O(1) time without resizing and O(n) time when resizing
    def push(self, data):
        if self.size == self.cap:
            tmp = self.stack
            self.cap *= 2
            self.stack = [None]*self.cap
            for i in range(self.size):
                self.stack[i] = tmp[i]
        self.stack[self.size] = data
        self.size += 1
    
    # Deletion runs in O(1) time always
    def pop(self):
        if self.is_empty():
            raise IndexError('Cannot pop an empty stack')
        self.size -= 1
        rc = self.stack[self.size]
        self.stack[self.size] = None
        return rc
```

## Code for Queue - Class

```python
class Queue:
    def __init__(self, cap = 10):
        self.data = [None]*cap
        self.cap = cap
        self.size = 0
        self.front = 0
        self.back = 0

    def capacity(self):
        return self.cap
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def is_empty(self):
        return self.size == 0

    # Insertion at the back O(1) time, O(n) when resizing
    def enqueue(self, data):
        if self.size == self.cap:
            tmp = self.data
            self.cap *= 2
            self.data = [None]*self.cap
            for i in range(self.size):
                self.data[i] = tmp[(tmp.front + 1) % self.cap]
            self.front = 0
            self.back = self.size
        self.data[self.back] = data
        self.back = (self.back + 1) % self.cap
        self.size += 1

    # Deletion at the front O(1) time
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue an empty queue')
        rc = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return rc
```

## Code for Dequeue - Class

```python
class Dequeue:
    def __init__(self, cap = 10):
        self.data = [None]*cap
        self.cap = cap
        self.size = 0
        self.front = 0
        self.back = 0
    
    def capacity(self):
        return self.cap
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.data[self.front]
    
    def get_back(self):
        if self.is_empty():
            return None
        return self.data[self.back]

    def is_empty(self):
        return self.size == 0

    # Resizing operation happens in O(n) time
    def resize(self):
        tmp = self.data
        self.cap *= 2
        self.data  = [None]*self.cap
        for i in range(self.size):
            self.data[i] = tmp[(self.front + i) % self.cap]
        self.front = 0
        self.back = self.size - 1
    
    # Insertion at front O(1) time, O(n) when resizing
    def push_front(seld, data):
        if self.size == self.cap:
            self.resize()
        if self.size != 0:
            self.front = (self.front - 1) % self.cap
        self.data[self.front] = data
        self.size += 1

    # Deletion operation at front O(1)
    def pop_front(seld, data):
        if self.size == 0:
            raise IndexError('Cannot pop front on empty dequeue')
        rc = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return rc
    
    # Insertion at back O(1) time, O(n) when resizing
    def push_back(seld, data):
        if self.size == self.cap:
            self.resize()
        if self.size != 0:
            self.back = (self.back + 1) % self.cap
        self.data[self.back] = data
        self.size += 1

    # Deletion operation at back O(1)
    def pop_back(seld, data):
        if self.size == 0:
            raise IndexError('Cannot pop back on empty dequeue')
        rc = self.data[self.back]
        self.data[self.back] = None
        self.back = (self.back - 1) % self.cap
        self.size -= 1
        return rc
```

## When should LISTs be used?

Lists are the most basic data structures there is, an ordered collection with a specified size. Typically, they are almost always used but there can be specific use cases for them too. So When should they be used?

| LIST Data Structures     | When is It Important to Use Them?                                      |
|--------------------------|------------------------------------------------------------------------|
| Arrays (unsorted)        | When random access to elements is required                             |
|                          | Having elements contiguous in memory is important, for utilizing cache |
|                          | Requires fast/frequent insertion but removal doesn't matter            |
|                          | Requires O(1) modification times and at least O(n) search times        |
| Linked Lists (unsorted)  | Random Access is important                                             |
|                          | Contiguous memory is not important                                     |
|                          | Requires fast insertion and fast removal, in O(1) time                 |
|                          | Requires O(1) modification time, O(n) search times is acceptable       |
| Stacks                   | When reversing strings                                                 |
|                          | Used for comparing the most recent value, so checking parentheses      |
|                          | When backtracking and managing the most recent state is important      |
|                          | Insertion and removal requires as fast as possible runtime             |
|                          | When search and modification operations won't be used                  |
| Queues                   | When ordering items based on insertion is important                    |
|                          | Handling asynchronous data is required, or simulating line-ups         |
|                          | Insertion and removal requires fast runtimes                           |
|                          | Search and modification are not needed                                 |

## Why should LISTs be used over other Data Structures?

Lists should be used when playing to the strengths of it's implementation. The idea of a list is to keep a collection of elements ordered based on the insertion of each element. This allows for fast insertion and sometimes removal as well, depending on if elements are removed from the back or front only. If the list is sorted then search times are O(log(n)) which is good for progressively larger data sizes. 

The greatest strength a list like data structure has is the random access nature of the data structure. If random access is important for modification, or search operations then list data structures should be used. It should also be used since computer memory behaves in a similar way and it allows the code to be implemented more easily.
- best for searching and modification of data
- random access of elements
- fast insertions and removal operations depending on behavior
- useful for implementing behavioral based storage
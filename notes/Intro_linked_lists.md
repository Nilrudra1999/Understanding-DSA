# Intro to Singly and Doubly Linked Lists

Linked list Data Structures are examples of List ADTs where data is stored within a sequence of linked nodes. Each node can be in it's own block of memory thus a linked list is never contiguous in memory unlike other data structures from list ADTs. Both a singly and doubly linked list have pointers which connect the various nodes in the list and pointers which point to nodes at the front and back of the list, creating a chain-like structure.

## Linked List Implementation

Both singly and doubly linked lists start-off with a default constuctor making an empty list.

```python
class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
```

The main differences between these list's implementation starts as the nested Node class gets implemented. Each linked list has a nested node class, thats in charge of holding the individual pieces of data within the list. For singly linked lists the nested node class only has a next pointer, but the doubly linked list class has nested nodes with both a next and previous pointers which connect to the next and previous nodes.

```python
class SinglyLinkedList:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    class Node:                     # nested node class
        def __init__(self, data):
            self.data = data
            self.next = None        # points to the next node
```

![Singly_LL](https://github.com/user-attachments/assets/1a7e7302-f9e0-44f1-9378-54e40aaf39d5)

```python
class DoublyLinkedList:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    class Node:                     # nested node class
        def __init__(self, data):
            self.data = data
            self.next = None        # points to the next node
            self.prev = None        # points to the previous node
```

![Doubly_LL](https://github.com/user-attachments/assets/71dba72a-b1e9-4196-b470-28f933558f82)

## Linked List Operation Runtimes

| Operations   | Array                       | Singly LL        | Doubly LL        |
|--------------|-----------------------------|------------------|------------------|
| push_front() | O(n)                        | O(1)             | O(1)             |
| push_back()  | O(1)                        | O(1)             | O(1)             |
| search()     | Linear O(n) Binary O(log n) | Linear only O(n) | Linear only O(n) |
| pop_front()  | O(n)                        | O(1)             | O(1)             |
| pop_back()   | O(n)                        | O(n)             | O(1)             |

From this we can conclude that, implementing a Stack and Queue using a linked list is possible. However, its best to avoid popping back on singly linked list because it has the worst runtime of any LL operations. So when using a LL as the underlying data structure the implementation should be done so that it avoids that operation.

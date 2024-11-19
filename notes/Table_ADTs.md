# Notes on TABLE Abstract Data Types

These notes will explore the following:
- ✅ What is a TABLE ADT?
- ✅ What are some implementations of TABLE ADTs?
- ✅ What does the code look like?
- When should TABLEs be used?
- Why should TABLEs be used over other Data Structures?

## What is a TABLE ADT?

An unordered collection of (key, value) pairs. The main idea behind a table is that its ordering is based on the keys being inserted into it. The key value pairs are also known as records, and within the same table ALL keys are UNIQUE. Even if values are duplicates, two keys can never be the same otherwise the previous key's value will be overwritten.

Thus the defining characteristics of TABLE ADTs are:
- they consist of (key,value) pairs
- its a collection of data much like a list ADT
- the ordering is determined by the keys being inserted not the order of insertion
- ALL keys must be unique, but values can have duplicates
- client code always provides both the keys and the associated values
- allows for insertion, search, modification, and removal in O(1) amortized runtime

## What are some implementations of TABLE ADTs?

Implementations of TABLE ADTs can vary, from key-based sorted lists, to hash tables, or trees. The simplest implementation is use an array sorted based on the keys being inserted. This implementation has a serious runtime drawback, where search() and modify() has a runtime of O(log n) but insert() has a runtime of O(n) and removal() is even worse.
- insert(key,value) - O(n)
- search(key) - O(log n)
- modify(key, value) - O(log n) + O(1)
- remove(key) - O(log n) + O(n)

On the other hand a Table implemented using an unsorted array:
- insert(key,value) - O(1)
- search(key) - O(n)
- modify(key, value) - O(n) + O(1)
- remove(key) - O(n) + O(1)

The implementation which fixes these runtime issues, is the hash table implementation.<br>
Which clocks in at an amortized runtime of O(1) across all operations.

## Hash Table Implementation and Code

Hash tables are implemented using hashing, which is done using hash functions, (treating them like a black-box) they take some value and convert it into an unsigned int which can mostly produce unique numbers. The runtime of this function is also independent of the number of records meaning for (n) records it has a constant number of operations. So using this function means O(1) time. Therefore:
- using a hash function we can take a key, map it to an unsigned int
- use the integer to store the value at an array index
- in constant time, and this hashing is used for all operations

The only issue is that sometimes when working with an array of a fixed size, collisions can occur.<br>
A Collision is when two keys are mapped to the same index, so where to place the second key?<br>

There exists two techniques to resolve this known as Closed and Open Addressing.<br>

### Closed Addressing (Chaining)

Chaining is the idea that in a closed addressing system declare an array of Linked list objects. Every "address" is an array index with a pointer to a LL object, where hash values are mapped by modding by capacity. The linked list object at each address ensures that we have a way to chain/link each new value on top of the existing ones.

![chaining](https://github.com/user-attachments/assets/26e87783-22f3-4b92-afd0-084c43ef6f4b)

Another way of reproducing this same system is using bucketing.<br>
Which is basically a 2D array, so a collision results in being stored in the 2nd dimension.

![chaining_with_2d_array](https://github.com/user-attachments/assets/eb4b44d7-2b81-4a2c-9f9c-b6d82bf00653)

### Open Addressing (Linear Probing)

Linear Probing is the idea of skipping over by an index everytime there is a collision, until an empty index if found. A process of finding "the next available address" given index n, indecies (n + i) are checked until another opening is found.

![linear_probing_demo01](https://github.com/user-attachments/assets/ee2f8823-753f-4dd4-a87a-885528ca5845)

```python
class HashTable:
    # This class manages the state of a parrallel and behavior of a function
    # Using strings as flags
    class State:
        def __init__(self):
            self.full = 'F'
            self.empty = 'E'
            self.deleted = 'D'
            self.insert = 'create'
            self.search = 'find'


    def __init__(self, cap = 10):
        self.arr_st = State()                   # tracks the state of the table
        self.flag = State()                     # flag that changes function's behavior
        self.table = [None] * cap               # empty list of records (the table)
        self.st = [self.arr_st.empty] * cap     # parrallel array tracking state
        self.cap = cap                          # capacity
        self.size = 0                           # used up space


    def insert(self, key, value):
        if self.size == self.cap:
            new_cap = self.cap * 2
            tmp_list = [None] * new_cap
            self.st = [self.arr_st.empty] * new_cap
            for i in range(self.size):
                key, value = self.table[i]
                index = self.find_spot(key, self.flag.insert)
                if index != None:
                    tmp_list[index] = self.table[i]
                    self.st[index] = self.arr_st.full
            self.table = tmp_list
            self.cap = new_cap
        index = self.find_spot(key, self.flag.insert)
        if index == None:
            raise ValueError('Trying to insert value with a duplicate key')
        else:
            self.table[index] = (key, value)
            self.st[index] = self.arr_st.full
            self.size += 1


    # Function either returns unsigned int (index of the key) or None
    def search(self, key):
        return self.find_spot(key, self.flag.search)


    def remove(self, key):
        index = self.search(key)
        if index != None:
            self.table[index] = None
            self.st[index] = self.arr_st.deleted
            self.size -= 1
            return True
        return False


    def modify(self, key, value):
        index = self.search(key)
        if index != None:
            self.table[index] = (key, value)
            return True
        return False


    def find_spot(self, key, flag):
        index = hash(key) % self.cap
        i = 0
        while self.table[index] != None:
            if self.st[index] != self.arr_st.deleted:
                ex_key, ex_value = self.table[index] 
                if ex_key == key and flag == self.flag.search:
                    return index
                elif ex_key == key and flag == self.flag.insert:
                    return None
            i += 1
            index = (hash(key) + i) % self.cap
        if self.table[index] == None and flag == self.flag.insert:
            return index
        elif self.table[index] == None and flag == self.flag.search:
            return None
```
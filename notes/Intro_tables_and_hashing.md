# Intro to Tables and Hashing

Abstract Data Types define a set of operations without defining their underlying data structure or implementation. Much like how lists are their own ADT, Tables are another Abstract Data Type. Tables ADTs are defined as the following:
- a collection of key-value pairs (records)
- these "records" store a key/identifier and a corresponding value
- this collection is NOT ordered, its just a collection of stuff
- but the keys are all unique (they have to be)
- insert(key,value) - adds a new key-value pair
- modify(key, value) - changes the value for a given key
- remove(key) - deletes a record with the matching key
- search(key) - find the value with that key

Depending on which of those operations are more important to users, the Table ADT class can be implemented using various different underlying data structures. Some underlying data structures will allow for faster searching at the cost of insertion or removal, while others allows for avg. runtimes across all operations. So when implementing the Table ADT class its important to understand the trade-offs between different underlying data structures, in terms of operational speed.

## Non-Hashed Table Implementations and Runtimes

If a Table was implemented using a sorted array the following would be true in-terms of runtimes of various operations:
- insert(key,value) - O(n)
- modify(key, value) - O(log n) + O(1)
- remove(key) - O(log n) + O(n)
- search(key) - O(log n)

On the other hand a Table implemented using an unsorted array, the following would be true in-terms of runtimes:
- insert(key,value) - O(1)
- modify(key, value) - O(n) + O(1)
- remove(key) - O(n) + O(1)
- search(key) - O(n)

Thus, in situations where Table ADTs require fast searching and modification at the cost of insertion and removal, using a sorted array as the underlying data structure is good. Places like a hospital's record system can use Tables implemented with sorted arrays, allowing them to search and modify patient records quickly. Unsorted arrays in contrast are a worse implementation of Table ADT classes, since searching is what Tables are usually built for and using an unsorted array means searching takes O(n) runtime.

## Hashing, Collision Resolution

So it is established that a non-hashed Table ADT implemeneted using a sorted array, allows for fast search and modify operations at the cost of insertion and removal operation runtimes. However, is there a way to make this Table ADT class's implementation such that, the runtimes of insertion and removal is also improved?

### Method 01 For Faster Operational Runtimes: Mapping Keys to a Direct Access Array

By mapping the keys related to the values inside a direct access array. Where the value of a key = n, is mapped to the nth index of that array, can achieve a faster insertion and removal runtime while still maintianing the fast searching runtime. However, if there is a million keys the direct access array would be a million indexs long, which is a problem, since its too much space storing all the keys.

### Method 02 For Faster Operational Runtimes: Using Hashing and Collisions

Hashing is done using hash functions, which takes a key and returns a hash value: an unsigned whole number (integer). Given a key it will always return the same Hash value, so the return value is consistent. The runtime of this function is also independent of the number of records meaning for (n) records it has a constant number of operations, so the runtime of this function is O(1). 
- using a hash function we can take any key, map it to an unsigned int
- store the value at that array index
- in constant time, and this hash function is used for all operations
- insertion, removal, modification, and search can all be implemented in O(1) runtime

```python
def insert(key,value):
    array_of_records = (key,value)                  # array of tuples, of (key,value)
    hash_index = hash_value % cap                   # hash value is given by the hash function
    array_of_records[hash_index] = (key, value)     # insert into that array index
```

The problem with this implementation is not the finding of hash values, but something known as collisions.<br>
Where two or more keys are mapped to the same hash value/index.<br>

To resolve this the following techniques for collision resolution are used:<br>
Closed Addressing:
- where multiple (key,value) records are stored inside the same index
- after hashing, we perform a search through the records at that index

Open Addressing:
- check arr[hash_value % cap] to see if its empty
- if not, then keep moving across until the "next" available spot
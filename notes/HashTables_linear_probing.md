# Intro to The Open Addressing Technique of Linear Probing

Opening addressing as a system is distinct from closed addressing because, where closed addressing allows multiple records to be stored at the same array index, open addressing doesn't allow that and opties to find the next available address given a hash_index which is occupied.

The process of finding "the next available address" comes in many forms.<br>
The simplest of which is Linear probing where, given index n, index (n+1) is checked until an open index is found.

## Implementing Linear Probing

The implementation of linear probing comes down to how the code handles insertion, removal, modification, and searching.<br>
Specifically when a collision occurs how does the code handle that scenario.<br>

```python
# how finding the index with the right key is handled with open addressing
def __find_key_index(key):
    hash_value = hash(key)
    hash_index = hash_value % cap
    for i in range(len(arr)):
        key = hash(hash_index % cap)
        if arr[hash_index].key == key:
            return hash_index
        elif arr[hash_index] == None:
            return hash_index
```

```python
# how insertion operations are handled with an open addressing system
def insert(key, value):
    index = __find_key_index(key)
    arr[index] = (key,value)
```

```python
# how search operations are handled with an open addressing system
def search(key):
    return __find_key_index(key)
```

```python
# how modification operations are handled with an open addressing system
def modify(key, value):
    index = __find_key_index(key)
    arr[index] = (key,value)
```

```python
# how removal operations are handled with an open addressing system
def remove(key):
    index = __find_key_index(key)
    arr[index] = None
    curr = index + 1 # go around if needed?
    while not is_empty(curr):
        # determine if record at current should be moved to arr[index]
        # is index between hash index of current and current index?
            arr[index] = arr[curr]
        curr = index + 1
```
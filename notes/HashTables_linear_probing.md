# Intro to The Open Addressing Technique of Linear Probing

Opening addressing as a system is distinct from closed addressing because, where closed addressing allows multiple records to be stored at the same array index, open addressing doesn't allow that and opties to find the next available address given a hash_index is occupied. A process of finding "the next available address" is Linear probing where, given index n, index (n + i) is checked until an open index is found.

## Implementing Linear Probing

The implementation of linear probing comes down to how the code handles insertion, removal, modification, and searching.<br>
Specifically when a collision occurs, how does the code handle that scenario?<br>

```python
class HashTable:
    def __init__(self, cap = 10):
        self.cap = cap
        self.size = 0
        self.table = [None] * cap

    def insert(self, key, value):
        if self.size == self.cap:
            new_cap = self.cap * 2
            temp_list = [None] * new_cap
            for i in range(self.cap):
                temp_list[i] = self.table[i]
            self.table = temp_list
            self.cap = new_cap
        index = find_spot(key, 'create')
        self.table[index].append((key, value))
        self.size += 1

    def search(self, key):
        return find_spot(key, 'find')

    def delete(self, key):
        index = find_spot(key, 'remove')
        if index:
            self.table[index] = 'T'
            self.size -= 1
            return True
        return False

    def modify(self, key, value):
        index = find_spot(key, 'update')
        if index:
            self.table[index][1] = value
            return True
        return False
    
    def find_spot(self, key, flag):
        pass    # yet to be implemented
```
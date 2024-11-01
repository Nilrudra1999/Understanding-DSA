# Intro to The Open Addressing Technique of Linear Probing

Opening addressing as a system is distinct from closed addressing because, where closed addressing allows multiple records to be stored at the same array index, open addressing doesn't allow that and opties to find the next available address given a hash_index is occupied. A process of finding "the next available address" is Linear probing where, given index n, index (n + i) is checked until an open index is found.

## Implementing Linear Probing

The implementation of linear probing comes down to how the code handles insertion, removal, modification, and searching.<br>
Specifically when a collision occurs, how does the code handle that scenario?<br>

```python
class HashTable:
    def __init__(self, cap = 10):
        self.cap = cap              # capacity
        self.table = [None] * cap   # empty list
        self.size = 0               # used up space


    def insert(self, key, value):
        if self.size == self.cap:
            new_cap = self.cap * 2
            temp_list = [None] * new_cap
            for i in range(self.size):          # len of all elements of the old array
                temp_list[i] = self.table[i]    # does resizing shuffle the elements? like in a queue
            self.table = temp_list
            self.cap = new_cap
        index = self.find_spot(key, 'create')
        if index == None:
            raise IndexError('Trying to create with duplicate key')
        else:
            self.table[index].append((key, value))
            self.size += 1


    def search(self, key):
        return self.find_spot(key, 'find')      # either returns unsigned int or None


    def delete(self, key):
        index = self.search(key)
        if index:
            self.table[index] = 'T'
            self.size -= 1
            return True
        return False


    def modify(self, key, value):
        index = self.search(key)
        if index:
            self.table[index] = (key, value)
            return True
        return False
    

    def find_spot(self, key, flag):
        index = hash(key) % self.cap
        i = 0
        while self.table[index] != None:
            if self.table[index] != 'T':
                ex_key, ex_value = self.table[index] 
                if ex_key == key and flag == 'find':
                    return index
                elif ex_key == key and flag == 'create':
                    return None
            i += 1
            index = (hash(key)+i) % self.cap
        if self.table[index] == None and flag == 'create':
            return index
        elif self.table[index] == None and flag == 'find':
            return None
```

![linear_probing_demo01](https://github.com/user-attachments/assets/ee2f8823-753f-4dd4-a87a-885528ca5845)

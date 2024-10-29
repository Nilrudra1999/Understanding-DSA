# Introduction to Graphs

Graphs are used to model data, where the most important thing is the relationship between the data.<br>
The formal definition of a graph is: G = (V,E) where each edge E defines a connection between (u,v) = V.<br>
This means that a graph is made of node/vertices and edges/connections between the nodes.<br>

Each vertex/node of a graph is an object and the edges represent the relationship between these objects.<br>
If we want to represent and store the information associated with an object and its connections to others, we can do so by creating a record and storing that record into a table. Specifically, a Hash Table, keeping in mind the method of insertion and searching.

Aside from identifying a connection between vertices, edges can also have weights.<br>
Digraphs also represent direction with their edges along with weights.<br>

## Adjacency Matrix

An adjacency matrix is in essence a 2 dimensional array which can be used to represent a Graph or store information about it. Where each vertex represent an index of the 2D array and the number of rows of the Adjacency Matrix represents the number of unique nodes of the Graph. The time complexity to find an edge is O(1) but the space complexity to store this data is O($n^2$).

### Graph Represented Using an Adjacency Matrix

```python
class Graph:
    def __init__(self, size = 10):
        self.size = size
        self.matrix = [[None]*size] * size
    
    def add_edge(self, src, dst):
        self.matrix[src][dst] = 1
    
    def check_edge(self, src, dst):
        return self.matrix[src][dst] == 1

    def print_graph(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j])
            print('')
```

## Adjacency List

Another way of representing a Graph is using an Adjacency List which is an array of LL objects. Each LL object inside an index of the array all have a unique node at the head of the linked list which represents a unique vertex. Then to form connections subsequent nodes are added which represent the other objects that are associated with the unique object, to form chain like connections. When adding an edge the node's address is added to the tail of the Linked list.

### Graph Represented Using an Adjacency Matrix

```python
import LinkedList

class Graph:
    def __init__(self, size = 10):
        self.size = size
        self.list = [LinkedList()] * size
    
    def add_node(self, node):
        self.list[self.size].push_back(node)

    def add_edge(self, src, dst):
        index = self.check(src)
        if index:
            self.list[index].push_back(dst)
            return True
        return False
    
    def check_edge(self, src):
        for i in range(len(self.list)):
            if self.list[i].get_front() == dst:
                return i
        return None

    def print_graph(self):
        for i in range(len(self.list)):
            j = self.list[i].get_front()
            while j != None:
                print(j + '--->')
                j = self.list[i].get_next()
            print('')
```
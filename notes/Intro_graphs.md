# Introduction to Graphs

What is the point of Graphs? and why should we even use this?

Graphs are used to model data, where the most important thing is the relationship between the data.<br>
The formal definition of a graph is: G = (V,E) where each edge E defines a connection between (u,v) = V.<br>
This means that a graph is made of node/vertices and edges/connections between the nodes.<br>

![basic_graph](https://github.com/user-attachments/assets/029318b4-b664-4ddb-8ed3-e0d0461e702e)

Each vertex/node of a graph is an object and the edges represent the relationship between these objects.<br>
If we want to represent and store the information associated with an object and its connections to others, we can do so by creating a record and storing that record into a table. Specifically, a Hash Table, keeping in mind the method of insertion and searching.

![edge_def](https://github.com/user-attachments/assets/3a5d100e-0df0-44d8-a6bf-b8759ab9e701)

Aside from identifying a connection between vertices, edges can also have weights.<br>
Digraphs also represent direction with their edges along with weights.<br>

![digraphs](https://github.com/user-attachments/assets/06d4518f-4a57-4ef0-81b1-6abdf20f74f3)

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
        index = self.check_edge(src)
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

## Dijkstra's Algorithm

This algorithm is used to measure the shortest distance from one node to every other node in the graph.<br>
Its used to digitally mapping shortest distance between nodes/objects which are connected to one another. Can be used to map locations in a city where the connections all represent roads/paths which can be taken to each node/location. At the beginning a single node is always picked from which to calculate paths to other nodes.

### Step 01 of This Algorithm

Two lists are created and a current node:
- visited Nodes []
- unvisited Nodes [A,B,C,D,E,F]
- curr_node = A

| Node | Shortest Distance | Previous Node |
|------|-------------------|---------------|
| A    | 0                 |               |
| B    | inf               |               |
| C    | inf               |               |
| D    | inf               |               |
| E    | inf               |               |
| F    | inf               |               |

### Step 02 of This Algorithm

Now its time to find the first shortest distance between two distinct nodes.<br>
Then update the table accordingly.
- visited Nodes [A]
- unvisited Nodes [B,C,D,E,F]
- curr_node = B (shortest distance from A)

| Node | Shortest Distance | Previous Node |
|------|-------------------|---------------|
| A    | 0                 |               |
| B    | 2                 | A             |
| C    | inf               |               |
| D    | 8                 | A             |
| E    | inf               |               |
| F    | inf               |               |

### Step 03 of This Algorithm

Next the pervious steps are repeated.<br>
The shortest distances are also set based on which is smaller, curr distance or the calculated distance.
- visited Nodes [A,B]
- unvisited Nodes [C,D,E,F]
- curr_node = D (shortest distance from B)

| Node | Shortest Distance | Previous Node |
|------|-------------------|---------------|
| A    | 0                 |               |
| B    | 2                 | A             |
| C    | inf               |               |
| D    | 2+5               | B             |
| E    | 2+6               | B             |
| F    | inf               |               |

### Step 04 of This Algorithm

Next the pervious steps are repeated.<br>
- visited Nodes [A,B,D]
- unvisited Nodes [C,E,F]
- curr_node = E (shortest distance from D)

| Node | Shortest Distance | Previous Node |
|------|-------------------|---------------|
| A    | 0                 |               |
| B    | 2                 | A             |
| C    | 8+9               | E             |
| D    | 7                 | B             |
| E    | 8                 | B             |
| F    | 9                 | D             |

### Step 05 of This Algorithm

Next the pervious steps are repeated.<br>
- visited Nodes [A,B,D,E]
- unvisited Nodes [C,F]
- curr_node = F (shortest distance from E)

| Node | Shortest Distance | Previous Node |
|------|-------------------|---------------|
| A    | 0                 |               |
| B    | 2                 | A             |
| C    | 12                | F             |
| D    | 7                 | B             |
| E    | 8                 | B             |
| F    | 9                 | D             |

### Step 06 of This Algorithm

Then the final node is marked as visited and the total distance is calculated.<br>
- visited Nodes [A,B,D,E,F]
- unvisited Nodes [C]
- curr_node = C (shortest distance from F)

| Node | Shortest Distance | Previous Node |
|------|-------------------|---------------|
| A    | 0                 |               |
| B    | 2                 | A             |
| C    | 12                | F             |
| D    | 7                 | B             |
| E    | 8                 | B             |
| F    | 9                 | D             |

Using the table we can now follow the shortest distance from each node to the other.<br>
According to the table to go from A to C we need to trace backwards starting at C.<br>
- C ---> F (prev node)
- F ---> D (prev node)
- D ---> B (prev node)
- B ---> A (prev node)

This represents a single calculation which is complete. This same table with the same information can now be used to map any shortest path from the node A to any other node. The question now is, what is the most effective method of storing the information of this table inside the computer? such that it can easily be searched to find the shortest path from A to any other node.
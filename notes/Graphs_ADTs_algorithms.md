# Notes on Graphs ADTs, Algorithms and Implementations

These notes will explore the following:
- ✅ What is a GRAPH ADT?
- ✅ What are some implementations of GRAPH ADTs?
- ✅ What does the code look like?
- ✅ When should GRAPHs be used?
- ✅ Why should GRAPHs be used over other Data Structures?

## What are Graphs?

Graphs are used to model the relationship between various pieces of data or objects. They consist of a set of vertices and edges, where the edges form the connections between the vertices and the vertices are the pieces of data or objects being modeled. An example can be, connecting various streets on a map from multiple locations.

The formal definition of a graph is: G = (V,E) where each edge E defines a connection between (u,v) = V.<br>
Each vertex/node (V) is an object and the edges (E) represent the relationship between these objects.<br>

![basic_graph](https://github.com/user-attachments/assets/029318b4-b664-4ddb-8ed3-e0d0461e702e)

Aside from identifying a connection between vertices, edges can also have weights.<br>
When the edges have a specified direction then these are known as digraphs.<br>

![digraphs](https://github.com/user-attachments/assets/06d4518f-4a57-4ef0-81b1-6abdf20f74f3)

The ability of graphs to model relations and networks can lend to a wide varity of real-world problem solutions. From modeling city and geographic maps, to modeling server networks and webpage redirection, graphs can be used to model relationships between entities and use this model to solve problems. Graphs also have some ADT specific features:
- when edges between one or more vertices connect in a loop it forms a cycle
- graphs can have both weights and direction which makes a digraph
- std graphs don't typically have direction but have weights
- finding the shortest path between nodes is known as MST (min spanning tree)
- these relationships are typically formed using a specialized data structure known as heaps
- when two nodes are connected they have adjacency
- social media networks are a good example of an undirected graph with adjacency
- users are represented using vertices, while a follow is represented by an edge
- when two users are connect by following each other, they are adjacent to one another
- depending on if they both follow each other or if one person follows the other
- one vertices can have adjacency while the other cannot
- this is an example of a directed graph

## Basic Graph Implementations

In-terms of basic implementation graphs can be implemented using an Adjacency Matrix or an Adjacency List.

### Adjacency Matrix

An adjacency matrix is in essence a 2 dimensional array. Where each row and each column represents a vertice and the values held in the cells are the connections between the vertices. For graphs without weights, a 1 represents a connection between two vertices, while a 0 represents no connection. For graphs with weights the weight value of the edge replaces the 0 value of no connection. Index [0,0] is always empty.

![adj_matrix_graphs](https://github.com/user-attachments/assets/ba878e5d-6322-41e4-b810-011f566f3d76)

```python
class Graph:    # A representation of a graph without weights
    def __init__(self, size = 10):
        self.size = size
        self.matrix = [[None]*size] * size
    
    def add_edge(self, src, dst):   # constant time insertion
        self.matrix[src][dst] = 1
    
    def check_edge(self, src, dst): # constant time look-up
        return self.matrix[src][dst] == 1

    def print_graph(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j])
            print('')
```

### Adjacency List

Another way of representing a Graph is using an Adjacency List which is an array of LL objects. Each index holds a pointer to the LL object and each LL object has a unique node at the head of the linked list which represents a unique vertex from which other vertices are connected to form edges. When adding an edge the node's address is added to the tail of the Linked list.

![adj_list_graphs](https://github.com/user-attachments/assets/8e8488a9-593a-4d12-9d65-2fdf0b89c456)

```python
import LinkedList

class Graph:
    def __init__(self, size = 10, nodes):
        if len(nodes) != size:
            raise ValueError('The list must be the same size as the number of Nodes')
        self.size = size
        self.list = [None] * size
        for i in range(self.size):              # The list is initialized first with LLs
            self.list[i] = LinkedList()         # Each new unique LL obj pointer is held
            self.list[i].push_back(nodes[i])    # all unique nodes are distributed
    
    # Adds a new unique node to the graph
    def add_node(self, node):
        self.list.append(LinkedList())
        self.list[self.size].push_back(node)
        self.size += 1

    def add_edge(self, src, dst):
        index = self.check_edge(src)
        if index != None:
            self.list[index].push_back(dst)
            return True
        return False
    
    # The runtime is at most O(V), representing the number of total vertices
    def check_edge(self, src):
        for i in range(self.size):
            if self.list[i].get_front() == src:
                return i
        return None

    def print_graph(self):
        for i in range(self.size):
            j = self.list[i].get_front()
            while j != None:
                print(j + '--->')
                j = self.list[i].get_next()
            print('')
```

## Dijkstra's Algorithm of Shortest Paths

This algorithm is used to measure the shortest distance from one node to every other node in the graph.<br>
Its used for mapping the shortest distance between nodes/objects which are connected to one another. At the beginning a single node is always picked from which to calculate paths to other nodes to. This algorithm gives the shortest path from any one node to any other node after its has been run on the whole graph.

![dij_graphs](https://github.com/user-attachments/assets/4e831881-0c96-4b89-90e5-62ccff6e0f56)

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

### How to Store This Information

The best method is to use two hash tables.<br>
The Shortest Distance Table, maps each node to its shortest known distance from the starting node.<br>

| Node | Shortest Distance |
|------|-------------------|
| A    | 0                 |
| B    | 2                 |
| C    | 12                |
| D    | 7                 |
| E    | 8                 |
| F    | 9                 |

And the Predecessor Table, maps each node to its previous node.<br>

| Node | Previous Node |
|------|---------------|
| A    | None          |
| B    | A             |
| C    | F             |
| D    | B             |
| E    | B             |
| F    | D             |
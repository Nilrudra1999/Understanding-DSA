# Notes and Intro on Minimum Spanning Trees, Tree ADT, and Related Algorithms

These notes will explore the following:
- ✅ What are TREEs and what is a MST?
- What are some implementations of TREEs or how are they stored?
- What does the code look like?
- ✅ When and why should TREEs be used?

## What is a Minimum Spanning Tree and How Can it be Made?

A Minimum Spanning Trees is a connected, acyclic subgraph derived from a graph where G = (V,E). It represents the shortest path through all nodes of a graph. If there was a city map with multiple locations represented by nodes and edges representing roads, then Dijkstra's Algorithm can be used to form a network of routes which when taken provides the shortest distance between any two points within the city. However, if someone wants to travel all the locations throughout the entire city then an MST can be used to represent the shortest path which covers all locations.

To find an MST, we can either start removing edges till we get an MST or selecting edges till we form an MST. Using the removal method we can start by removing edges with the highest weights until all vertices are connected by edges without having any cycles and all edges have the lowest possible weights. This is an impractical method since for (n) nodes in a graph, a spanning tree has (n-1) edges min, or as many as $\frac{(n)(n-1)}{2}$ edges. Thus, this method usually gets completed in quadratic time.

Instead we can use a greedy method for finding the MST for any graph.<br>
These methods include Prim's Algorithm and Kruskal's Algorithm.<br>

### Prim's Algorithm

This method finds the MST by starting at one node and branching out.<br>
While carrying out this procedure its adviced to use a MinHeap to store the results.<br>
We queue into this heap, edges that will connect an isolated vertex (the root).

### Kruskal's Algorithm.

This method finds the MST by simultaneously searching the entire graph for lowest edges.<br>
The smallest edge weights are added first, followed by the next set of low edge weights.<br>
Until all nodes are connected.

## What is a TREE then?

A tree is a data structure more so than an ADT, but it can also be understood as an ADT as well. A tree's purpose is to categorize information such that the overhead on searching is reduced to a single operation. The reason why trees can be understood as both ADT and data structure is because there are various types of trees. Binary, complete, full, and etc however, they all follow the same structure which is implementation specific.
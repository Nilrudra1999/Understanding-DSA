# Intro to Minimum Spanning Trees

A Minimum Spanning Trees is a connected, acyclic subgraph derived from a graph where G = (V,E).<br>
Lets consider a graph with the following representation. A collection of verties connected by edges.<br>
G = (V,E)<br>
where V = [1,2,3,4,5,6]<br>
where E = [(1,2),(2,3),(3,4),(4,5),(5,6)]

In this above example the subgraph, represented by S can be expressed as Es = E-1.<br>
Where E represents the number of edges of the original graph and Es represents the edges of the subgraph.<br>
S = (V,Es)<br>
where V = [1,2,3,4,5,6]<br>
where E = [(1,2),(2,3),(3,4),(4,5)]

Depending on the spanning tree's starting point the number of edges are reduced by 1, in this case.<br>
There are however, more complex trees and greedy methods of calculating min cost subgraphs.

## Prim's Algorithm

A Greedy method which connects all verties of a graph such that it forms a subgraph.<br>
The subGraph specifically has the lowest cost edges that form a path to all verties.
- select min cost edge of the graph
- select another min cost edge which is connected to prev edge verties
- keep doing this until all verties are connceted 
- subgraph should be G = (V,E-1)

## Kruskal's Algorithm

Another Greedy method which connects all verties of a graph such that it forms a subgraph.<br>
- min cost edges are selected multiple times
- from multiple different locations, without the need for connecting prev verties
- only those min cost edges are selected which don't form cycles
- subgraph should be G = (V,E-1)
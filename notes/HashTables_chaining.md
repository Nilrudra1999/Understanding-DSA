# Intro to The Closed Addressing Technique of Chaining

Chaining is the idea that in a closed addressing system we can declare an array of Linked list objects.<br>
Every "address" is a hash value modded using the capacity of the array.<br>
The linked list object at each address ensures that we have a way to chain/link each new value on top of the existing ones.

### Some Problems With Chaining

1. The nodes take up space for 2 pointers and the data
2. Each array index includes an entire object 
3. usually a LL object is stored in main memory rather than cache
4. accessing a LL increases runtime, even if O(1) operations are done
5. LLs need to be searched/sorted before insertion

The problems with this implementation then really arise with the utilization of the Linked List object itself. The array might actually be stored at a fast to access memory location but the linked list objects, or more accurately the nodes of the linked list object may be kept on the heap in main memory, increasing runtimes. 

This can be subsituted with a 2D array, where hashable indexes point to columns and individual cells in each row is where the values are kept. Running out of cells adds (x) number of rows and running out of hasable indexes adds (y) number of columns. But then resizing would take O(x*y) runtime and similar space complexity increases.
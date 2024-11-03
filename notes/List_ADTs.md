# Notes on LIST Abstract Data Types

These notes will explore the following:
- What is a LIST ADT?
- What are some implementations of LIST ADTs?
- What does the code look like?
- When should LISTs be used?
- Why should LISTs be used over other Data Structures?
- How are some LIST data structures the same?
- How are they different?

## What Are Some LIST ADTs

### First lets define what an Abstract Data Type is

```
An Abstract Data Type, is the concept of a way of storing information inside a computer without the implementation details. It defines which operations this storage can perform and what sort of behavior the storage will have without specifying how the code would work or structurally what it'll look like.
```

LIST ADTs are defined as the following, but some LISTs don't follow all aspects of this definition:
- Collection of data that has some ordering
- The data is either stored Contiguously or linked in sequence
- The data can be traversed either Bidirectional or Unidirectional
- The data can be randomly accessed or have behavioral restrictions
- Allows insertion operations (with or without behavioral restrictions)
- Allows Searching operations
- Allows Modifying operations (with or without behavioral restrictions)
- Allows Removal operations (with or without behavioral restrictions)
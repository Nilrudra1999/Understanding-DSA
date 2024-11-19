# Notes on TABLE Abstract Data Types

These notes will explore the following:
- ✅ What is a TABLE ADT?
- ✅ What are some implementations of TABLE ADTs?
- What does the code look like?
- When should TABLEs be used?
- Why should TABLEs be used over other Data Structures?

## What is a TABLE ADT?

An unordered collection of (key, value) pairs. The main idea behind a table is that its ordering is based on the keys being inserted into it. The key value pairs are also known as records, and within the same table ALL keys are UNIQUE. Even if values are duplicates, two keys can never be the same otherwise the previous key's value will be overwritten.

Thus the defining characteristics of TABLE ADTs are:
- they consist of (key,value) pairs
- its a collection of data much like a list ADT
- the ordering is determined by the keys being inserted not the order of insertion
- ALL keys must be unique, but values can have duplicates
- client code always provides both the keys and the associated values
- allows for insertion, search, modification, and removal in O(1) amortized runtime

## What are some implementations of TABLE ADTs?

Implementations of TABLE ADTs can vary, from key-based sorted lists, to hash tables, or trees. The simplest implementation is use an array sorted based on the keys being inserted. This implementation has a serious runtime drawback, where search() and modify() has a runtime of O(log n) but insert() has a runtime of O(n) and removal() is even worse.
- insert(key,value) - O(n)
- search(key) - O(log n)
- modify(key, value) - O(log n) + O(1)
- remove(key) - O(log n) + O(n)

On the other hand a Table implemented using an unsorted array:
- insert(key,value) - O(1)
- search(key) - O(n)
- modify(key, value) - O(n) + O(1)
- remove(key) - O(n) + O(1)

The implementation which fixes these runtime issues, is the hash table implementation.<br>
Which clocks in at an amortized runtime of O(1) across all operations.

## Hash Table Implementation and Code
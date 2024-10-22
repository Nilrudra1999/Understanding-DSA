# Understanding Linear and Binary Search Algorithms

Linear and Binary search are some of most basic searching algorithms used to look for data within array like Data Structure. What exactly they are? How they are written in code? Why they are important? and Where they are best used? are the topics of this following note.

## Linear Search

The most basic searching algorithm where an simple iterator increments through an array and we check each element's value against a target value. During the search if the value is found we return the index at which it was found, or if not then we return -1 or 0.<br>
Linear searches don't require the array to be pre-sorted and they make use of the random access nature of an array.<br>
The runtime of this algorithm is O(n) since the algorithm's loop runs for the size of the array, which is (n).

```python
def linear_search(arr, data):
    for i in range(0, len(arr)):    # simple iterator moves through the array
        if arr[i] == data:          # matching values
            return i
    return -1                       # if the value doesn't exist then we return -1
```

The reason why linear search algorithms are important, is because of a few reasons:
1. allows searching on unsorted arrays, saves sorting runtime
2. simple to write and faster on smaller arrays than binary search
3. usable on singly or doubly linked lists

## Binary Search

The second fundamental type of searching algorithm, is the binary search. This search looks for a target value by taking the highest and lowest indices within an array and finding their middle first. Then it compares the middle index's value with the target value. If the target value is lower than the middle index then, the highest index is decreased to the current middle index - 1. If the target value is higher than the middle index then, the lowest index is increased to the current middle index + 1. This way we can cut the effective search area for the value within the array by half each time we compare, and if the value is not found, or the highest and lowest indices cross then we return -1.

The runtime of this algorithm is O(log(n)) since given an array of size (n) is cuts the size by half each iteration so it only runs log(n) iterations.

```python
def binary_search(arr, data):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low+high) // 2       # setting the mid
        if arr[mid] > data:
            high = mid - 1          # if data is less than mid value
        elif arr[mid] < data:
            low = mid + 1           # if data is more than mid value
        elif arr[mid] == data:
            return mid              # data found
    return -1
```

Reasons why binary search algorithms are important, is because of a few reasons:
1. Has a fast runtime when working with larger array's
2. Has a faster runtime than linear search especially with larger arrays

## Best Places to Use These Algorithms

These algorithms are meant specifically for searching through things.<br> 
Thus they can be used in any abstract manner to search through a list of something.<br>

Linear Searches:
- doesn't require the list of stuff to be sorted
- but does take O(n) time, so it's runtime scales with the size of the list

Binary Searches:
- requires pre-sorting so a little more extra work beforehand
- but when the list of things are sorted then this takes the least runtime

Abstractly, both of these algorithms can run on lists of things of any size. However, the deciding factor is, if the list of things are sorted or not. The bigger the list the better binary search does, granted that the list is sorted, while linear search does better with smaller lists and doesn't need sorting. Linear search as a concept also works with singly and doubly linked lists while binary doesn't.
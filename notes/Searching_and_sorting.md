# Notes on Searching and Sorting Algorithms

These notes will explore the following:
- ✅ What are these algorithms?
- ✅ What does the code look like?
- ✅ When should these algorithms be used?
- ✅ Why should these algorithms be used?

## What are these algorithms?

As the name implies, searching algorithms search for data inside a data structure.<br>
While sorting algorithms sort the data thats stored inside a data structure.<br>

Some common problems they solve are:
- looking for something specific in random data takes a while, how to fix that?
- how can a computer find specific pieces of data?
- how can we decrease the total amount of time needed to find data inside a collection?
- how can we order data based on our own rules and not insertion order?

### Types of Searching Algorithms

There are only two types of searching algorithms, Linear and Binary Search.<br>

| Algorithms    | What it is                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Linear Search | Searches a list like data structure from start to finish, this is a brute force algorithm <br>which iterates one by one through all the different elements of a list. It exits when it finds <br>the value returning its index, or it returns -1 (value not found). Can be used with any <br>list DS, sorting doesn't matter.                                                                                                                                                                                                                                                                                                   |
| Binary Search | This search starts by comparing the middle index of a list like data structure with the <br>value we're looking for. If the value is bigger than the middle we ignore the lower half of the <br>list and perform the same search on the upper half of the list. If the value is smaller than <br>the middle we ignore the upper half of the list and perform the same search on the lower half. <br>This keep going until we either find the value and return the index or return -1. This algorithm <br>can be used only with a contiguous list like DS and it must be sorted based on whatever <br>data we're searching for.  |

### Types of Sorting Algorithms

There are two groups of sorting algorithms, simple sorts and complex sorts.<br>
Among simple sorting algorithms there are, bubble, insertion, and selection sorts.<br>

| Algorithms     | What it is                                                                                                                                                                                                                                                                                                                                              |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bubble Sort    | This sort repeatedly steps through a list, comparing two adjacent elements and swapping them<br>if they are in the wrong order. This allows the algorithm to bubble the largest values to the<br>back of the list. It swaps values once throughout the list for every element the list has.<br>Thus, taking O(n) time at best and O(n^2) time at worst. |
| Insertion Sort | Insertion sort builds a sorted list one element at a time, by taking each element and inserting<br>it into the correct position in a sorted region. Has the same runtime as bubble sort.                                                                                                                                                                |
| Selection Sort | This algorithm divides the list into sorted and unsorted regions. It then repeatedly finds the<br>smallest or largest elements in the unsorted region and swaps it with the first element of that<br>region. It iterates once throughout the list for each element the list has.                                                                        |

Then among the complex sorting algorithms there are, quick and merge sorts.<br>

| Algorithms | What it is                                                                                                                                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quick Sort | Quick sort partitions the array into two parts based on a pivot element, elements smaller<br>than the pivot are placed to the left and elements greater than the pivot are placed to the <br>right. This process is repeated recursively for both left and right subarrays until the array<br>is sorted and joined together. |
| Merge Sort | Merge sort splits the array into halves, then recursively sorts them, merging the sorted <br>parts of the subarrays. This algorithm guarantees a O(n log n) sort time complexity.                                                                                                                                            |

## When Should These Algorithms be Used and Why?

Throughout the runtime of a program there are variables and values which need to be stored however, the reason for storing these values is because we need to retrieve and use them later. This is where search algorithms come into play, they allow us to retrieve the data which is stored in data structures like lists so that we can use those values for computation. 

So the problem being solved by search algorithms is that of "retrieval for usage".<br>
But this can sometimes be slow if the data structure is really big, so the second problem is speed.<br>

This is where sorting algorithms come into play. We can utilize binary search which is much faster than linear search if and only if the list we're working with is sorted. Sorting takes time but if the list is sorted now then searches performed on it later will take less time for larger and larger sized data.

### Thus, Why Should Searching and Sorting be Used

1. It allows us to store data for retrieval and usage later
2. Allows the stored data to be sorted based on our rules/usage
3. Sorted data is easier and faster to search thus our programs takes less time to compute

### When Should Searching and Sorting be Used

1. Linear searches should be used with smaller data sizes
2. Binary searches are faster the larger the data size gets
3. Sorting is required before binary search can be used
4. Simple sorts should be used when memory is tight and in-place sorting is necessary
5. Complex sorts should be used when memory is plentiful and time matters more

## Code for Linear Search Algorithm

```python
def linear_search(arr, data):
    for i in range(0, len(arr)):    # simple iterator moves through the array
        if arr[i] == data:          # matching values
            return i
    return -1                       # if the value doesn't exist then we return -1
```

## Code for Binary Search Algorithm

```python
def binary_search(arr, data):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low+high) // 2   # setting the mid
        if arr[mid] > data:
            high = mid - 1      # if data is less than mid value
        elif arr[mid] < data:
            low = mid + 1       # if data is more than mid value
        elif arr[mid] == data:
            return mid          # data found
    return -1
```

## Code for Quick Sort Algorithm

```python
def quick_sort(arr, start, end):
    if end <= start:                    # We have nothing left to sort
        return
    pivot = partition(arr, start, end)  # make the first sort and find the pivot
    quick_sort(arr, start, pivot-1)     # call recurivsely using the pivot
    quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = len(arr)
    i = start -1
    for i in range(start, end):
        if arr[j] < pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    i += 1
    tmp = arr[i]
    arr[i] = arr[end]
    arr[end] = tmp
    return i    # return the pivot
```

## Code for Merge Sort Algorithm

```python
def merge_sort(arr):
    size = len(arr)
    if size <= 1:
        return
    mid = size // 2                     # spliting the array down the middle
    left_array = [None] * mid           # initializing the first sub-array
    right_array = [None] * size - mid   # initializing the second sub-array
    i = 0   # left array
    j = 0   # right array
    while i < size:
        if i < mid:
            left_array[i] = arr[i]
        else:
            right_array[i] = arr[i]
            j += 1
        i += 1
    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, arr)

def merge(lefta, righta, arr):
    left_size = len(arr) // 2
    right_size = len(arr) - left_size
    i = 0
    l = 0
    r = 0
    # sorting the sub_array
    while l < left_size and r < right_size:
        if lefta[l] < righta[r]:
            arr[i] = lefta[l]
            i += 1
            l += 1
        else:
            arr[i] = righta[r]:
            i += 1
            r += 1
    while l < left_size:
        arr[i] = lefta[l]
        i += 1
        l += 1
    while r < right_size:
        arr[i] = righta[r]
        i += 1
        r += 1
```

## Code for Bubble Sort Algorithm

```python
def bubble_sort(arr):
    n = len(arr)
    # Outer loop sorts the overall list
    for i in range(n):
        # Inner loop sorts the sub-region of the list
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr
```

## Code for Insertion Sort Algorithm

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
    return arr
```

## Code for Selection Sort Algorithm

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if arr[m] > arr[j]:
                m = j
            tmp = arr[i]
            arr[i] = arr[m]
            arr[m] = tmp
    return arr
```
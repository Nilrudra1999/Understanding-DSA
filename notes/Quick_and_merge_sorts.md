# Understanding Quick and Merge Sorting

A slightly more complicated algorithm than the simple sorts are Quick and Merge sort.<br> 
This note explores what they are? why they are used? how they are written? and when to use them?<br>

## Quick Sort Algorithm

Quick sort as an algorithm, sorts an array of some List like ADT with random access using the concept of a pivot. We usually start the pivot at then end of the array, and find the final resting place for the pivot (a value). Then with simple iterators, usually i and j, are compared to one another each time the a loop iterates. After comparison, any swaps occur using a temp variable while also checking if the value of j is always less than the pivot. 

The goal here is to use i as the resting point for the smaller values in each comparison and use j as the resting point for any larger values in each comparison. All the while the pivot is also compared to j each time meaning when j becomes smaller than the pivot the pivot and j switch positions.

Quick sort is a recursive sorting algorithm, so once the pivot switches positions, we call the function itself. By passing a low and high index tracker for each sub-section of the array, before and after the recently set pivot. The array is still in place. This sorting algorithm in it's worst case can run in O($n^2$) however, in its best and avg cases it can run in O(nlog(n)) time complexity.

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
        if arr[j] < pivot:          # compare j and i and swap
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    i += 1                          # index the final time for swapping
    tmp = arr[i]
    arr[i] = arr[end]
    arr[end] = tmp
    return i                        # return the pivot
```

The use case for this algorithm are:
1. using the divide and conquer method can achieve a good runtime
2. highly efficient the bigger the array size

## Merge Sort Algorithm

Merge sort is another complex sorting algorithm, using the divide and conquer method.<br>
Using recursion to divide our current array into 2 sub-arrays and call the merge sort function again. Then we keep doing this until each array only has 1 index element remaining, at which point we sort the individual arrays and merge them back together. Much like quick sort this sorting algorithm also has a runtime complexity of O(nlog(n)).

```python
def merge_sort(arr,):
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
    while l < left_size and r < right_size: # sorting the sub_array
        if lefta[l] < righta[r]:
            arr[i] = lefta[l]
            i += 1
            l += 1
        else:
            arr[i] = righta[r]:
            i += 1
            r += 1
    while l < left_size:                    # sorting the left most element
        arr[i] = lefta[l]
        i += 1
        l += 1
    while r < right_size:                   # sorting the right most element
        arr[i] = righta[r]
        i += 1
        r += 1
```

The use cases for this algorithm are:
1. using the divide and conquer method can achieve a good runtime
2. highly efficient the bigger the array size
3. can be implemented with a clean interface for the client

## When to Use These Algorithms

These algorithms have a better time comeplexity than the simple sorting algorithms like insertion, selection, and bubble sort. However, these algorithms have a worse space complexity than the simple sorting algorithms, since both quick and merge sort use recursion to sort the arrays. So the use cases of these algorithms come down to the trade off between time and space, if space is not an issue then using these sorts will save time, especially with larger data sets.
# Introduction to Iteration and Recursion

These notes will explore the following:
- ✅ What is Iteration and Recursion?
- ✅ What does the code look like?
- ✅ When should iteration be used vs recursion?
- ✅ Why should iteration be used over recursion?

## What is Iteration and Recursion?

### Iteration

Iterative algorithms use a block of code known as a "loop" to repeatedly perform a task(s), multiple times. They exit either after some condition is fulfilled or the computation it was performing gets completed. Generally, loops have a runtime complexity of O(n) where (n) represents the length of some value or set of data which the loop iterates over. Nested loops have a runtime complexity of O($n^a$) where (a) represents the number of loops running in total. This is because every single time a loop is nested the outer loop runs (n) times and the inner runs (n) times independently for each iteration of the outer loop.

If however the inner loop is dependent on the outer loop like shown below:

```python
def function(n):
    total = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            total += 1
    print(total)
```

Then we need to use a formula from the arithemtic series to solve for this.<br>
$\frac{n}{2}(2a + (n-1)d)$ Second formula:<br>
- Where (n) represents the number of iterations the outer loop has
- (a) represents the first number of iterations of the inner loop (just the value itself)
- (d) represents the difference between each iteration of the inner loop

### Recursion

Recursion on the other hand, is used to perform similar functions to a loop, where some tasks or set of tasks are repeated until some exit condition is met. The difference, is that recursion works by calling the same function over and over again. This is a much more dangerous method of solving an iterative problem, since this could lead to a stack overflow from too many function calls if the exit condition is not met. Though both methods can reach similar runtimes, recursion has an O(n) space complexity where (n) represents total number of function calls made on the stack, while iteration has a O(1) space complexity since it solves for the problem in-place.

![runtime_stack_and_recursion_image](https://github.com/user-attachments/assets/8ab04020-bb5b-416a-859c-6724f9a81483)

## Some Iterative Algorithm Code and Analysis

### Iterative Algorithm One

Let n represent the value of the number passed to the function<br>
Let S(n) represent the total number of operations done by the function given n<br>

```python
def sum_natural_numbers(n):
    total = 0                   # 1
    for i in range(1, n+1):     # n + 1
        total += i              # 1 * n
    return total                # 1
```

$S(n) = 1 + (n+1) + n + 1$<br>
$S(n) = 2n + 3$<br>
Therefore, S(n) is O(n) linear time complexity

### Iterative Algorithm Two

Let n represent the length of a list passed to the function<br>
Let B(n) represent the total number of operations done by the function given n<br>

```python
def bubble_sort(arr):
    n = len(arr)                    # 1
    for i in range(n):              # n + 1
        for j in range(0, n-i-1):   # (n(n-1))/2 + 1 (loop iterations using arithmetic series formula)
            if arr[j] > arr[j+1]:   # 1 * (n(n-1))/2
                                    # best case 0 assigns
                                    # avg case log n assigns
                                    # worst case (n(n-1))/2                      
                arr[j] = arr[j+1]   # 2 * (n(n-1))/2
                arr[j+1] = arr[j]   # 2 * (n(n-1))/2
    return arr                      # 1
```

Using the worst case senario to make the analysis we assume that the statements nested inside the (if) run everytime the loop runs.<br>
$B(n) = 1 + (n+1) + (\frac{n(n-1)}{2} + 1) + \frac{n(n-1)}{2} + n(n-1) + n(n-1) + 1$<br>
$B(n) = \frac{n(n-1)}{2} + \frac{n(n-1)}{2} + 2(n(n-1)) + n + 4$<br>
$B(n) = n(n-1) + 2(n(n-1)) + n + 4$<br>
$B(n) = 3n^2 -2n + 4$<br>
Therefore, B(n) is O($n^2$) quadratic time complexity

## Some Recursive Algorithm Code and Analysis

Let n represent the value we pass to the function<br> 
Let T(n) represent the number of operations done by fact() given n as an argument<br>

```python
def fact(n):
    rc = 1                  # 1
    if n > 1:               # 1
        rc = n * fact(n-1)  # 3 + T(n-1)
                                # 3 operators not in a loop
                                # T(n-1) because that is the cost of fact(n-1) call
    return rc               # 1
```

$T(n) = 1 + 1 + 3 + T(n-1) + 1$<br>
$T(n) = T(n-1) + 6$<br>
$T(n-1) = T((n-1)-1) + 6$<br>
$T(n-1) = T(n-2) + 6$<br>

$T(n) = T(n-2) + 6 + 6$<br>

$T(n-2) = T(n-3) + 6$<br>
$T(n-3) = T(n-4) + 6$<br>
$T(n-4) = T(n-5) + 6$ when n > 1<br>

when n <= 1 but >= 0 then<br>
$T(0) = 3$<br>
$T(1) = 3$<br>
Because the base case for the function exits after 3 operations.<br>
But eventually we get to a number like T(2) after reducing (n) number of times<br>

$T(2) = T(1) + 6$<br>
$T(2) = 3 + 6$<br>
$T(3) = 3 + 6 + 6$<br>
So the pattern that emerges is the following:<br>
$T(n) = 3 + 6(n-1)$<br>
$T(n) = 3 + 6n - 6$<br>

$T(n) = 6n - 3$ for n > 1<br>
Therefore, T(n) is O(n) linear complexity for all values of n > 1.

## When should iteration be used vs recursion and why?

Both can be used to perform searching operations on data structures.<br>
Both can be used to perform sorting operations on data structures.<br>
They can also both be used for simulating mathematical operations.<br>

### Iteration Specific Use Cases

- searching when data structures exceed a certain size, because iteration is in-place
- sorting when data structures exceed a certain size
- infinite loops
- skipping the code block, when necessary
- performing Breath-First-Search

### Recursion Specific Use Cases

- Traversing hierarchical data structures, like trees or graphs
- performing Depth-First Search
- achieving better runtimes for sorting using divide and conquer algorithms

In general, iterative algorithms take longer to run vs recursive algorithms so for sorting recursion may be better. However, the downside of recursion is that it take more memory thus, when using them on excessively large data structures, stack overflows can be an issue. In the end it comes down to the trade offs between time and memory.

There are some data structure specific implementations for recursion vs iteration. Since recursion innately has a stack like nature its easier to implement this algorithm for searching trees and graphs, while iteration is much easier to implement for list like data structures because of its linear nature.
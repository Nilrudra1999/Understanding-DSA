# More Iterative Analysis on Common Iteration Functions

Below are further analysis on more common iterations using both for-loops and while loops.<br>
However, for the analysis there is no timing experiments provided.

### Function 01

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

### Function 02

Let n represent the length of an array passed to the function<br>
Let R(n) represent the total number of operations performed by the function given n<br>

```python
def reverse_array(arr):
    n = len(arr)                # 1
    for i in range(n // 2):     # n/2 + 1
        arr[i] = arr[n-i-1]     # 3 * n/2
        arr[n-i-1] = arr[i]     # 3 * n/2
    return arr                  # 1
```

$R(n) = 1 + (\frac{n}{2} + 1) + 3\frac{n}{2} + 3\frac{n}{2} + 1$<br>
$R(n) = \frac{n}{2} + 3n + 3$<br>
Therefore, R(n) is O(n) linear time complexity

### Function 03

Let n represent the length of a list passed to the function<br>
Let M(n) represent the total number of operations done by the function given n<br>

```python
def find_max(arr):
    max_value = arr[0]      # 1
    for i in arr:           # n
        if i > max_value:   # 1 * n
            max_value = i   # best case 0 assigns: loop is sorted in descending order
                            # avg case log n assigns: as loop iterates chance of new max diminishes
                            # worst case n-1 assigns: since (if) is true for all elements after the 1st
    return max_value        # 1
```

We model the expression using the worst case senario so we model (max_value = i) using (n-1)<br>
$M(n) = 1 + n + n + (n-1) + 1$<br>
$M(n) = 3n + 1$<br>
Therefore, M(n) is O(n) linear time complexity

### Function 04

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

### Function 05

Let n represent the number is_prime() is trying finding a prime for<br>
Let P(n) representing the total number of operations done by the function given n<br>
We analyze for all values where n > 1<br>

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):   # (sqrt(n)-1) + 1 (** operator is for exponentiation)
                                            # best case (if) is true 1 time
                                            # avg case (if) is true log n times
                                            # worst case (if) is true 0 times
        if n % i == 0:                      # 1 * sqrt(n)-1 (worst case)
            return False                    # 1
    return True                             # 1
```

$P(n) = (\sqrt{n}-1) + 1 + (\sqrt{n}-1) + 1 + 1$<br>
$P(n) = 2(\sqrt{n}-1) + 3$<br>
$P(n) = 2\sqrt{n} + 1$<br>
Therefore, P(n) is O(sqrt(n)) square root of n time complexity

### Function 06

Let n represent the smaller number between (a) and (b)<br>
Let G(n) represent the total number of operations done by gcd() given n<br>

```python
def gcd(a, b):
    while b != 0:   # log(n)
        a = b       # 1 * log(n)
        b = a % b   # 2 * log(n)
    return a        # 1
```

$G(n) = log(n) log(n) + 2log(n) + 1$<br>
$G(n) = 4log(n) + 1$<br>
Therefore, G(n) is O(log(n)) logarithmic time complexity

### Function 07

Let n represent the target number passed to the function to count digits till<br>
Let D(n) represent the total number of operations done by the function given n<br>

```python
def count_digits(n):
    count = 0           # 1
    while n != 0:       # log_10(n) n is reduced by 10 each iteration
        n //= 10        # 1 * log_10(n)
        count += 1      # 1 * log_10(n)
    return count        # 1
```

$D(n) = 1 + \log_{10}(n) + \log_{10}(n) + \log_{10}(n) + 1$<br>
$D(n) = 3\log_{10}(n) + 2$<br>
Therefore, D(n) is O($\log_{10} n$) base 10 logarithmic time complexity

## General Categories of Iterative Functions

Typical there seems to be 2 major categories of iterative algorithms that have different behaviors.<br> 
Single and Nested loops.<br>

### Single Loops

In this category we for-loops and while-loops of the following kinds
- for(start, end) or for(end) or for(range) which all behave the same way
- for(start, end, iterative interval) behaves differently since i skips the range at certain intervals
- while(condition) this has the most differing behvaiors so cycles need to be counted

### Nested Loops

In this category we can either have independent nested loops or dependent nested loops
- independent nested for loops is basically n * n in terms of behavior
- same goes for while loops that are nested and independent, with while loop counting
- dependant nested for loops is about using the arithmetic series formula to count the inner loop
- same goes for while loops that are nested and dependent, with while loop counting
# More Iterative Analysis on Common Iteration Functions

Below are further analysis on more common iterations using both for-loops and while loops.<br>
However, for the analysis there is no timing experiments provided.

## Function 01

Let n represent the number passed to the function<br>
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
Therefore, S(n) is O(n) Linear complexity

## Function 02

Let n represent the number the function needs to find a factorial for<br>
Let F(n) represent the total number of operations done by the function given n<br>

```python
def factorial(n):
    result = 1                  # 1
    for i in range(1, n+1):     # n + 1
        result *= i             # 1 * n
    return result               # 1
```

$F(n) = 1 + (n+1) + n + 1$<br>
$F(n) = 2n + 3$<br>
Therefore, F(n) is O(n) Linear complexity

## Function 03

Let n represent the length of the array passed to the function<br>
Let R(n) represent the total number of operations performed by the function given n<br>

```python
def reverse_array(arr):
    n = len(arr)                                    # 1
    for i in range(n // 2):                         # n/2 + 1
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]     # 2 * n/2
    return arr                                      # 1
```

$R(n) = 1 + (\frac{n}{2}+1) + 2(\frac{n}{2}) + 1$<br>
$R(n) = \frac{n}{2} + n + 3$<br>
Therefore, R(n) is O(n) linear complexity

## Function 04

Let n represent the target number for the fibonacci sequence for this function<br>
Let f(n) represent the total number of operations done by the function given n<br>

```python
def fibonacci(n):
    a, b = 0, 1                 # 2
    fib_sequence = []           # 1
    for _ in range(n):          # n + 1
        fib_sequence.append(a)  # 1 * n
        a, b = b, a + b         # 3 * n
    return fib_sequence         # 1
```

$f(n) = 2 + 1 + (n+1) + n + 3n + 1$<br>
$f(n) = 5n + 5$<br>
Therefore, f(n) is O(n) linear complexity

## Function 05

Let n represent the length of the list passed to the function<br>
Let M(n) represent the total number of operations done by the function given n<br>

```python
def find_max(arr):
    max_value = arr[0]      # 1
    for i in arr:           # n
        if i > max_value:   # 1
            max_value = i   # 1 * n
    return max_value        # 1
```

$M(n) = 1 + n + 1 + n + 1$<br>
$M(n) = 2n + 3$<br>
Therefore, M(n) is O(n) linear complexity

## Function 06

Let n represent the length of the list passed to the function<br>
Let C(n) represent the total number of operations performed by the function given n<br>

```python
def count_occurrences(arr, x):
    count = 0                   # 1
    for i in arr:               # n
        if i == x:              # 1 * n
            count += 1          # 1 * n
    return count                # 1
```

$C(n) = 1 + n + n + n + 1$<br>
$C(n) = 3n + 2$<br>
Therefore, C(n) is O(n) linear complexity

## Function 07

Let n represent the length of the list passed to the function<br>
Let B(n) represent the total number of operations done by the function given n<br>

```python
def bubble_sort(arr):
    n = len(arr)                                        # 1
    for i in range(n):                                  # n + 1
        for j in range(0, n-i-1):                       # (n(n-1))/2 + 1
            if arr[j] > arr[j+1]:                       # 1 * (n(n-1))/2                       
                arr[j], arr[j+1] = arr[j+1], arr[j]     # 2 * (n(n-1))/2
    return arr                                          # 1
```

$B(n) = 1 + (n+1) + (\frac{n(n-1)}{2} + 1) + \frac{n(n-1)}{2} + n(n-1) + 1$<br>
$B(n) = 2n^2 -2n + 4$<br>
Therefore, B(n) is O($n^2$) quadratic complexity

## Function 08

Let n represent the number the function is trying to check for prime<br>
Let P(n) representing the total number of operations done by the function given n<br>
For the analysis we will calculate the worst possible case<br>

```python
def is_prime(n):
    if n <= 1:
        return False                        # best case
    for i in range(2, int(n ** 0.5) + 1):   # sqrt(n) + 1
        if n % i == 0:                      # 2 * sqrt(n)                
            return False                    # avg case
    return True                             # 1
```

$P(n) = 2\sqrt{n} + \sqrt{n} + 1 + 1$<br>
$P(n) = 3\sqrt{n} + 2$<br>
Therefore, P(n) is O(sqrt(n)) root of n complexity

## Function 09

Let n represent the quotient from the division of (a) and (b)<br>
Let G(n) represent the total number of operations done by function given n<br>

```python
def gcd(a, b):
    while b != 0:           # a(log_b(n))
        a, b = b, a % b     # 3 * a(log_b(n))
    return a                # 1
```

$G(n) = a(log_b(n)) + 3(a(log_B(n)) + 1$<br>
$G(n) = 4a(log_b(n)) + 1$<br>
Therefore, G(n) is O(log(n)) logarithmic complexity

## Function 10

Let n represent the target number passed to the function to count digits till<br>
Let D(n) represent the total number of operations done by the function given n<br>

```python
def count_digits(n):
    count = 0           # 1
    while n != 0:       # log_10(n)
        n //= 10        # 1 * log_10(n)
        count += 1      # 1 * log_10(n)
    return count        # 1
```

$D(n) = 1 + \log_{10}(n) + \log_{10}(n) + log_n(10) + 1$<br>
$D(n) = 3\log_{10}(n) + 2$<br>
Therefore, D(n) is O($\log_{10} n$) logarithmic complexity

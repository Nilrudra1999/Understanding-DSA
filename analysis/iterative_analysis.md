## Analysis of simple_loop()

Let n represent the value of the number passed to the function
Let T(n) represent the total number of operations done by the function given n 

```python
def simple_loop(n):
    total = 0                   # 1
    for i in range(2, n+3):     # (n+1) + 1
        total += i              # 1 * (n+1)
    return total                # 1
```

$T(n) = 1 + (n+1) + 1 + (n+1) + 1$<br>
$T(n) = 2n + 5$<br>
Therefore, T(n) is O(n) Linear time complexity

## Analysis of skip_loop()

Let n represent the value of the number passed to the function
Let T(n) represent the total number of operations performed by the function given n

```python
def skip_loop(n):
    total = 0                   # 1
    for i in range(1, n+1, 3):  # (n/3) + 1
        total += i              # 1 * (n/3)
    return total                # 1
```

$T(n) = 1 + \frac{n}{3} + 1 + \frac{n}{3} + 1$<br>
$T(n) = \frac{2n}{3} + 3$<br>
Therefore, T(n) is O(n) Linear time complexity

## Analysis of nested_loop()

Let n represent the value of the number passed to the function
Let T(n) represent the total number of operations done by the function given n

```python
def nested_loop(n):
    total = 0                       # 1
    for i in range(1, n+4):         # (n+3) + 1
        for j in range(1, i+2):     # ((n+4)(n+5))/2 + 1
            total += j              # 1 * ((n+4)(n+5))/2
    return total                    # 1
```

$T(n) = 1 + (n+3) + 1 + \frac{(n+4)(n+5)}{2} + 1 + \frac{(n+4)(n+5)}{2} + 1$<br>
$T(n) = (n+4)(n+5) + (n+3) + 4$<br>
$T(n) = n^2 + 10n + 27$<br>
Therefore, T(n) is O($n^2$) quadratic time complexity

## Analysis of other_nested_loop()

Let n represent the value of the number passed to the function
Let T(n) represent the total number of operations done by the function given n

```python
def other_nested_loop(n):
    total = 0                       # 1
    for i in range(1, n+4):         # (n+3) + 1
        for j in range(1, n+5):     # (n+3)(n+4) + 1
            total += j              # 1 * (n+3)(n+4)
    return total                    # 1
```

$T(n) = 1 + (n+3) + 1 + (n+3)(n+4) + 1 + (n+3)(n+4) + 1$<br>
$T(n) = 2(n+3)(n+4) + (n+3) + 4$<br>
$T(n) = 2n^2 + 15n + 31$<br>
Therefore, T(n) is O($n^2$) quadratic time complexity
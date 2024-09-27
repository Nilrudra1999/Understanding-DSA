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

$T(n) = 1 + (n+1) + 1 (n+1) + 1$<br>
$T(n) = 2n + 5$<br>
Therefore, T(n) is O(n) Linear time complexity

![Time complexity of simple_loop()](https://github.com/user-attachments/assets/60d9c245-fa00-428f-ad30-fba49d5e6e1e)

## Analysis of skip_loop()

Let n represent the value of the number passed to the function
Let T(n) represent the total number of operations performed by the function given n

```python
def skip_loop(n):
    total = 0                       # 1
    for i in range(1, n+1, 3):      # (n/3) + 1
        total += i                  # 1 * (n/3)
    return total                    # 1
```

$T(n) = 1 + \frac{n}{3} + 1 + \frac{n}{3} + 1$<Br>
$T(n) = \frac{2n}{3} + 3$<br>
Therefore, T(n) is O(n) Linear complexity

![Time complexity of skip_loop()](https://github.com/user-attachments/assets/1649452b-7629-4bd1-960e-d1a8acbc3e3b)

## Analysis of nested_loop()

Let n represent the value of the number passed to the function
Let T(n) represent the total number of operations done by the function given n

```python
def nested_loop(n):
    total = 0                       # 1
    for i in range(1, n+4):         # (n+3) + 1
        for j in range(1, i+2):     # ((n+3)/2)(n+6) + 1
            total += j              # 1 * ((n+3)/2)(n+6)
    return total                    # 1
```

Calculating inner-loop:<br>
$\frac{n}{2}(2a + (n-1)d)$<br>
$\frac{n+3}{2}(2(2) + ((n+3) - 1)(1))$<br>
$\frac{n+3}{2}(n+6)$<br>

$T(n) = 1 + (n+3) + 1 + \frac{n+3}{2}(n+6) + 1 + \frac{n+3}{2}(n+6) + 1$<br>
$T(n) = (n+3)(n+6) + (n+3) + 4$<br>
$T(n) = n^2 + 10n + 25$<br>
Therefore, T(n) is O($n^2$) quadratic complexity

![Time complexity of nested_loop()](https://github.com/user-attachments/assets/b66a3e39-c6c9-43f0-82f9-801ee8b35b47)

## Analysis of other_nested_loop()

Let n represent the value of the number passed to the function
Let T(n) represent the total number of operations done by the function given n

```python
def other_nested_loop(n):
    total = 0                       # 1
    for i in range(1, n+4):         # (n+3) + 1
        for j in range(1, n+5):     # (n+4)(n+3) + 1
            total += j              # 1 * (n+4)
    return total                    # 1
```

$T(n) = 1 + (n+3) + 1 + (n+4)(n+3) + 1 + (n+4) + 1$<br>
$T(n) = n^2 + 9n + 23$<br>
Therefore, T(n) is O($n^2$) quadratic complexity

![Time complexity of other_nested_loop()](https://github.com/user-attachments/assets/2ad688ef-ff6f-47ff-821d-79935502c730)

## Analysis on Function 1: greet()

Let T(n) represent the total number of operations performed by greet()

```python
def greet():
    print("Hello world!")   # 1
```

$T(n) = 1$<br>
Therefore, T(n) is O(1) constant time.<br>
Each time greet() is called it always takes the same amount of time to process.

## Analysis on Function 2: apples()

Let n represent the value passed to the function<br>
Let T(n) represent the total number of operations done by the function apples()

```python
def apples(n):
    total = n * 5   # 2
    return total    # 1
```

$T(n) = 2 + 1$<br>
$T(n) = 3$<br>
Therefore, T(n) is O(1) constant time complexity.<br>
Here each line of the function only takes a constant amount of time.

## Analysis on Function 3: fruit()

Let n represent the value passed to the function<br>
Let T(n) represent the total number of operations done by fruit()

```python
def fruit(n):
    total = apples(n)   # 1 + 1
    return total        # 1
```

$T(n) = 1 + 1 + 1$<br>
$T(n) = 4$<br>
Therefore, T(n) is O(1) constant time complexity.<br>
Here we do account for the time taken by apples() as part of the analysis, but since its time complexity is O(1), it doesn't depend on n. Which is why the call to the function is counted but not in relation to n but as a single constant value.

## Analysis on Function 4: adding()

Let n represent the value of the number passed to the function<br>
Let T(n) represent the total number of operations performed by adding()

```python
def adding(x):
    sum = 0                 # 1
    n = (x*x)/2             # 1 + 1 + 1
    m = (x*x)/4             # 1 + 1 + 1
    for i in range(n):      # n + 1
        sum += 1            # 1 * n
    for j in range(m):      # m + 1
        sum += 1            # 1 * m
    for k in range(m+8):    # (m+8) + 1
        sum += 1            # 1 * (m+8)
    return sum              # 1
```

$T(n) = 1 + 3 + 3 + (n+1) + n + (m+1) + m + ((m+8)+1) + (m+8) + 1$<br>
$T(n) = 11 + 16 + 2n + 4m$<br>
$T(n) = 2n + 4m + 27$<br>
$n = \frac{x^2}{2} m = \frac{x^2}{4}$<br>
$T(n) = 2(\frac{x^2}{2}) + 4(\frac{x^2}{4}) + 27$<br>
$T(n) = 2x^2 + 27$<br>
Therefore, T(n) is O($x^2$) quadratic time complexity.<br>
Here there are 3 loops, 2 of which iterate using 2 different variables, where each variable represents the number of iterations of the loops. Loop 1 iterates for n times, loop 2 iterates for m times, and loop 3 iterates for m+8 times, where both (n) and (m) are dervied from (x).

## Aanalysis on Function 5: add_list()

Let n represent the length of the list passed to the function<br>
Let T(n) represent the total number of operations done by add_list()

```python
def add_list(list):
    total = 0                   # 1
    for i in range(len(list)):  # n + 1 + 1
        total += list[i]        # 1 * n
```

$T(n) = 1 + n + 2 + n$<br>
$T(n) = 2n + 3$<br>
Therefore, T(n) is O(n) linear time complexity.<br>
The function above iterates for the length of the list being passed to it. So from i=0 ... i=(n-1) which means it iterates for n times, thus whatever value is passed to the function the function will iterate for that number of times.
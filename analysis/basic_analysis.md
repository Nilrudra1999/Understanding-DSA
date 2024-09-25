## Analysis on Function 1: greet()

Let T(n) represent the total number of operations performed by greet()

```python
def greet():
    print("Hello world!")   # 1
```

$T(n) = 1$<br>
Therefore, T(n) is O(1) constant time.<br>
Each time greet() is called it always takes the same amount of time to process.

![Time complexity graphed for function greet()](https://github.com/user-attachments/assets/e780ea57-42ea-4b58-a9d1-2bbe7589c6d8)

## Analysis on Function 2: apples()

Let n represent the value passed to the function<br>
Let T(n) represent the total number of operations done by apples() given n

```python
def apples(n):
    total = n * 5   # 2
    return total    # 1
```

$T(n) = 2 + 1$<br>
$T(n) = 3$<br>
Therefore, T(n) is O(1) constant time complexity.<br>
Here each line of the function only takes a constant amount of time.

![Time complexity graphed for function apples()](https://github.com/user-attachments/assets/1f5c4c62-1808-4767-8e23-258f41f95f6f)

## Analysis on Function 3: fruit()

Let n represent the value passed to the function<br>
Let T(n) represent the total number of operations done by fruit() given n

```python
def fruit(n):
    total = apples(n)   # 1 + 1
    return total        # 1
```

$T(n) = 1 + 1 + 1$<br>
$T(n) = 4$<br>
Therefore, T(n) is O(1) constant time complexity.<br>
Here we do account for the time taken by apples() as part of the analysis, but since it's time complexity is O(1), it doesn't depend on n. Which is why the call to the function is counted but not in relation to n but as a single constant value.

![Time complexity graphed for function fruit()](https://github.com/user-attachments/assets/c2f864c8-d1dc-4453-89e0-ebbb10e62dbb)

## Analysis on Function 4: adding()

Let x represent the value of the number passed to the function<br>
Let n represent the value derived from x for the number of iterations for a loop<br>
Let m represent the value derived from x for the number of iterations for a loop<br>
Let T(x) represent the total number of operations performed by adding() given x

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

$T(x) = 1 + 3 + 3 + (n+1) + n + (m+1) + m + ((m+8)+1) + (m+8) + 1$<br>
$T(x) = 11 + 16 + 2n + 4m$<br>
$T(x) = 2n + 4m + 27$<br>
$n = \frac{x^2}{2}$ $m = \frac{x^2}{4}$<br>
$T(x) = 2(\frac{x^2}{2}) + 4(\frac{x^2}{4}) + 27$<br>
$T(x) = 2x^2 + 27$<br>
Therefore, T(x) is O($x^2$) quadratic time complexity.<br>
Here there are 3 loops, 2 of which iterate using 2 different variables, where each variable is derived from x which the value of the number passed to this function.

![Time complexity for function adding()](https://github.com/user-attachments/assets/4b3ef862-328c-41b9-ba36-3effc3807b39)

## Aanalysis on Function 5: add_list()

Let n represent the length of the list passed to the function<br>
Let T(n) represent the total number of operations done by add_list() given n

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

![Time complexity for function add_list()](https://github.com/user-attachments/assets/854be0af-9f6c-448c-a71c-6556fca9027d)

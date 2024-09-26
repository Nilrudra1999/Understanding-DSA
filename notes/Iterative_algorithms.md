# Iterative Functions and Algorithms Analysis

A lot of functions and algorithms use iteration to accomplish tasks. Iteration comes in the form of loops such as for-loop and while-loops which are embedded into the structure of an algorithm, where some instructions are executed multiple times based on the loop's parameters.

## Loop Structures Across Multiple Languages

The general syntax varys a little across languages however, the way programs are executed from one language to another also makes a difference in the analysis of that piece of code.

### Python

```python
for i in range(1, n+1): # n + 1
    # something         # 1 * n
```

In python, we can count the number of times the loop will run as i=1 ... i=(n+1) thus the loop will run (n) times.<br>
The we also add 1 for calling the range function which has a constant time complexity O(1).<br>
When the range() function is called we can typically calculate the number of times a loop will run in relation to (n). If the loop adds a third parameter for the range function like so: range(1, y+1, 2) we can take the initial runtime and divide it by that number, which is the value used to iterate through the loop.

### C++

```Cpp
for(int i=1; i < (n+1); i++) {  // 1 + n + (n+1)
    // something                // 1 * n
}
```

In C++, the loop's condition takes many steps. First is the assignment (int i=1), then is the iterations (i++), and finally it's the condition check (i < (n+1)). Thus, when constructing the loop we add 1 + (n) + (n+1) for assignment + iterations + condition checks.

### JavaScript

```Javascript
for(let i=1; i < (n+1); i++) {  // 1 + n + (n+1)
    // something                // 1 * n
}
```

In JavaScript the analysis of the loop is the same as in C++, since the loop is constructed in the same manner.<br>
Here too we have an assignment, a condition check, and an iteration.

## Mathematics Behind Nested Loops

There are 2 main types of nested loops:
- Ones where the inner loop is related to the outer loop
- Ones where the inner loop runs independent of the outer loop's value

If the inner loop runs independent of the outer loop's value then we count the number of iterations for the outer loop and multiple that to the number of iterations for the inner loop. That gives us the total number of iterations the inner loop makes.

However, if the inner loop is dependent on the outer loop then we need to count the number of total iterations made by the inner loop each time the outer loop iterates which requires counting the loops and using the arithmetic series formula to sub the correct values in for the iterations.

```python
def fun(n):
    total = 0                       # 1
    for i in range(1, n+2):         # (n+1) + 1
        for j in range(1, i+4):     # ((n+1)(n+8))/2 + 1
            total += 1              # 1 * ((n+1)(n+8))/2
    print(total)                    # 1
```

To calculate the inner loop we first find the value till which (i) iterates till in relation to (n). Which is n+1 in this case<br>
Then we find the value (j) iterates till in relation to (i) and we sub (n) for the relationship between (i) and (j)<br>
$i = n+1$ and $j = i+3$<br>
$j = \frac{m(m+1)}{2}$ where $m = n+1$<br>
$j = \frac{(n+1)(n+2)}{2}$<br>
$j = \frac{(n+1)(n+2)}{2} + 3(n+1)$<br>
$j = \frac{(n+1)((n+2)+6)}{2}$<br>
$j = \frac{(n+1)(n+8)}{2}$<br>

$T(n) = 1 + (n+1) + 1 + \frac{(n+1)(n+8)}{2} + 1 + \frac{(n+1)(n+8)}{2} + 1$<br>
$T(n) = (n+1)(n+8) + n + 5$<br>
$T(n) = n^2 + 10n + 13$<br>
Therefore, T(n) is O($n^2$) quadratic time complexity.

### Now lets test this formula and method using an edge case.

First edge case:<br>
Here we start again by finding what (i) and (j) loop till in relation to (n) and (i) respectively.

```python
def fun(n):
    total = 0                   # 1
    for i in range(n+1):        # (n+1) + 1
        for j in range(i+5):    # ((n+1)(n+10))/2 + 1
            total += 1          # 1 * ((n+1)(n+10))/2
    print(total)                # 1
```

$i = n+1$ times and $j = i+5$ times<br>
We sub $j = i+5$ for (n)<br>
$i = \frac{n(n+1)}{2}$ where i loops from i=0 till i=n<br>
Then we multiply the constant by the number of time (i) loops for so $5(n+1)$<br>
$j = \frac{n(n+1)}{2} + 5(n+1)$<br>
$j = \frac{(n+1)(n+10)}{2}$<br>

$T(n) = 1 + (n+1) + 1 + (n+1)(n+10) + 1 + 1$<br>
$T(n) = n^2 + 12n + 15$<br>
Therefore, T(n) is O($n^2$).

This method works with 2 components;
- the value of (i) at the end of all iterations in relation to (n)
- the total number of iterations (i) goes through in relation to (n)

Those values are then subbed into the total number of iterations (j) goes through in relation to (i);
- j = i + c where (c) is some constant
- (i) gets subbed by the arithmetic series formula where (n) is replaced by i = value in relation to (n) at the end of iterations
- the constant then gets multiplied by total number of iterations (i) goes through and added to the other bit
# Iterative Functions and Algorithms Analysis

Most programs use some form of iteration to solve a problem. Iteration comes in the form of loops such as for-loops/while-loops, which are embedded into the structure of an algorithm, where some instructions are executed multiple times based on the loop's parameters. The result of which can be used as a solution to a problem.

## Loop Structures Across Multiple Languages

The general syntax varys a little across languages however, most loops always have two basic components. A condition which is checked (n+1) times and a set of nested instructions which are executed (n) times.

### Python Loop

```python
for i in range(1, n+1): # n + 1
    # something         # n(1)
```

In python, we can count the number of times the loop will run as i=1 ... i=(n+1) thus the loop will run (n) times, but it checked (n+1) times.<br>
We add 1 for calling the range function which has a constant time complexity O(1).<br>
The number of times the loop will run in relation to (n) can be calculated as such: (n-y + x) where (y) is the starting point of the loop and (x) is the ending point of the loop.<br>

### C++ Loop

```Cpp
for(int i=1; i < (n+1); i++) {  // 1 + n + (n+1)
    // something                // 1 * n
}
```

In C++, the loop's condition takes more steps. First is the assignment (int i=1)<br>
Then is the iterations (i++)<br>
Finally the condition check (i < (n+1)).<br>
Thus, when constructing the loop we add 1 + (n) + (n+1) for assignment + iterations + condition checks.<br>

## Mathematics Behind Nested Loops

There are 2 main types of nested loops:
- Ones where the inner loop is related to the outer loop
- Ones where the inner loop runs independent of the outer loop's value

When the inner loop runs independent of the outer loop like shown below:

```python
for i in range(n):
    for j in range(n):
        # something
```

We find the total number of times the inner loop runs, and multiply that inner loop's iterations by the outer loop's iterations.<br>
So in this case n * n = inner loops iterations.<br>

If however the inner loop is dependent on the outer loop like shown below:

```python
def fun1(n):
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
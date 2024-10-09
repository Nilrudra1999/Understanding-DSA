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

When the inner loop runs independent of the outer loop like shown below:

```python
for i in range(n):
    for j in range(n):
        # something
```

Then to find the total number of times the inner loop ran we multiply the inner loop's iterations by the outer loop's iterations.<br>
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

The we need to use some formulas from the arithemtic series to solve for this.<br>
$\frac{n}{2}(a + l)$ First formula:<br>
- Where (n) represents the number of iterations the outer loop has
- (a) represents the first number of iterations of the inner loop
- (l) represents the last number of iterations of the inner loop

$\frac{n}{2}(2a + (n-1)d)$ Second formula:<br>
- Where (n) represents the number of iterations the outer loop has
- (a) represents the first number of iterations of the inner loop
- (d) represents the difference between each iteration of the inner loop
- Here we are subbing (l) for (d)

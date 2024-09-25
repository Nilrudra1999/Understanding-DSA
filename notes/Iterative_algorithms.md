# Iterative Functions and Algorithms Analysis

A lot of functions and algorithms use iteration to accomplish tasks. Iteration comes in the form of loops such as for-loop and while-loops which are embedded into the structure of an algorithm, where some instructions are executed multiple times based on the loop's parameters.

## Loop Structures Across Multiple Languages

The general syntax varys a little across languages however, the way programs are executed from one language to another also makes a difference in the analysis of that piece of code. Thus, we need to take a basic loop structure from one language and translate it to other languages to view the differences, in both syntax and analysis.

### Python

```python
for i in range(1, n+1): # n + 1
    # something         # 1 * n
```

In python, we can count the number of times the loop will run as i=1 ... i=(n+1) thus the loop will run (n) times.<br>
The we also add 1 for calling the range function which has a constant time complexity O(1).<br>
When the range() function is called we can typically calculate the number of times a loop will run in relation to (n) using this formula $n - y + x$. Where range(y, n + x), so in the case of the above code we could say $n - 1 + 1 = n$. If the loop adds a third parameter for the range function like so: range(1, y+1, 2) we can take the initial formula and divide it by that number, which is the value used to iterate through the loop.

### C++

```Cpp
for(int i=1; i < (n+1); i++) {  // 1 + n + (n+1)
    // something                // 1 * n
}
```

In C++ however, the loop's condition takes many steps, first is the assignment (int i=1), then is the iterations (i++), and then it's the condition check (i < (n+1)). Thus, when constructing the loop we add 1 for the assignment (n) for the number of times the loop runs, and (n+1) always for the condition check, since the check occurs onces more than the loop itself.

### JavaScript

```Javascript
for(let i=1; i < (n+1); i++) {  // 1 + n + (n+1)
    // something                // 1 * n
}
```

In JavaScript the analysis of the loop is the same as in C++, since the loop is constructed in the same manner.<br>
Here too we have an assignment, a condition check, and an iteration.

## Mathematics Behind Nested Loops

When a loop is nested within another loop, the inner loop iterates for the sum of the number of times the outer loop iterates. Meaning that if the outer loop iterates for n = 3 times the inner loop will iterate for n = 1 + 2 + 3 times which is n = 6. The inner loop's iterations can be calculated using the formula from the arithemtic series (n(n+1))/2 where (n) is substituted for the number of iterations the inner loop takes individually.

```python
for i in range(n):      # n
    for j in range(i):  # n(n-1)/2
        # something
```

In the above code snippet, the inner iterates from j=0 ... j=(n-1) and the outer loops iterates for (n) times individually, but the inner loop together with the outer loop runs (n(n+1))/2 times substituted for (n-1). Thus, the inner loop iterates for (n(n-1))/2 times.

```python
for i in range(n):      # n
    for j in range(n):  # n
        # something
```

In this other code snippet above, both loops run for (n) times however, the inner loop runs for (n) multipled the outer loop so ($n^2$).

```python
for i in range(n):          # n
    for j in range(i+1):    # n(n+1)/2
        # something
```

In this case, the inner loop runs till (n) instead of till (n-1) since the condition of the loop makes it so that it iterates for the nth time. Thus instead of substituting (n) inside (n(n+1))/2 for (n-1), in this case we substitute just (n).
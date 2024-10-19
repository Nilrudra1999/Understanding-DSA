# More Recursion Notes, Functions, and Analysis

First starting off with the steps to performing recursive analysis.<br>
Using an example used in the pervious recursion notes, we break down the analysis into more steps.<br>

```python
def fact(n):
    rc = 1
    if n > 1:
        rc = n * fact(n-1)
    return rc
```

### Step 01

Count the static statements like:
- return statements
- simple assignments
- anything that has a constant time complexity to execute

### Step 02

Declaring variables, which is even more important in recursive analysis.<br>
Since the variables will become the backbone of the base expression used to find the recursive pattern.<br>

### Step 03

If there is an If statements or any conditional statements, they always run ones, per recursive call.<br>
Within a loop that if statement may run ones every time the loop runs so (1 * n).<br>

### Step 04

When you get to the recursion statement count how many operators there are.<br>
Then using the an expression figure out how the function call is being made:<br>
- is the call T(n-1) or T(n-2)
- how many times is the call made?
- if the call is made with (n-1) 2 times then the expression should be T(n-1) + T(n-1)

### Step 05

Then establish the final expression with all the constants and the function call.<br>
Add up all the constant values and leave the T(n) call in-front of the expression and now we solve that.<br>
Then we sub T(n-k) where k is a constant, into T(n)'s expression, and we try to establish a pattern.<br>
- if T(n) = T(n-1) + 6
- and T(n-1) = T(n-2) + 6
- then T(n) = T(n-2) + 6 + 6
- and so on T(n) = T(n-k) + 6 + 6 ... + 6

### Step 06

To stop overselves from going on infinitely we find what the base case is and count the constant number of operations for that case.<br>
We stop usually when n <= 1 so when n = 0 or when n = 1.<br>
So when n does eventually reach 1 from being subtracted by k a certain number of times, what is the value of T(n)<br>
- T(1) = number of operations | counting conditions, assignments, and returns
- T(0) = number of operations | same thing
We count just before the base case and replace T(n-k) with the base case:<br>
- T(n) = T(2) + 6 ... + 6
- T(2) = T(1) + 6
- T(n) = T(1) + 6 + 6 ... + 6
- T(1) = 3 operations in total
- T(n) = 3 + 6 + 6 ... + 6 (now how many 6s do we have)
- in this case 6(n-1) so final expression is
- T(n) = 3 + 6n - 6
- T(n) = 6n - 3 for n > 1

### Step 07 

Now to state the therfore statement so we state the big O notation.<br>
Therefore, T(n) is O(n) and so on.

## More Complicated Function Using Recursion

Power function using recursion.

```python
def power(base, n):
    rc = base
    if n > 1:
        return rc = base * power(n-1)
    return rc
```
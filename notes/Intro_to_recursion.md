# Introduction to Recursion, Analysis and Implementations

The simplest recursively written function is the factorial function, which can also be written using a for-loop.<br>
A Recursive function is a function which finds a solution to a problem by calling itself.<br>

In the case of the factorial function:<br>
When n (the value being passed to the function for which we need a factorial for) is eqaul to 5<br>
5! = 5 * (4 * 3 * 2 * 1)<br>
5! = 5 * 4!<br>

However 4! = 4 * 3!<br>
And we can keep doing this on and on until we reach the 1st term.<br>

Thus, we can simplify the operations of the function down to the following.<br>
n! = n * (n-1) * (n-2) ... * 1<br>
And from this we build a base case (something all recursive functions need to stop calling itself)<br>
In this function the base case can be {if n is > 1 then factorial is also > 1}<br>

```python
def fact(n):
    rc = 1
    if n > 1:
        rc = n * fact(n-1)
    return rc
```

![runtime_stack_and_recursion_image](https://github.com/user-attachments/assets/8ab04020-bb5b-416a-859c-6724f9a81483)

## Analysis of This or Any Recursive Function

Let n represent the value we pass to the function<br> 
Let T(n) represent the number of operations done by fact() given n as argument<br>

```python
def fact(n):
    rc = 1                  # 1
    if n > 1:               # 1
        rc = n * fact(n-1)  # 3 + T(n-1)
                                # 3 operators not in a loop
                                # T(n-1) because that is the cost of fact(n-1) call
    return rc               # 1
```

$T(n) = 1 + 1 + 3 + T(n-1) + 1$<br>
$T(n) = T(n-1) + 6$<br>
$T(n-1) = T((n-1)-1) + 6$<br>
$T(n-1) = T(n-2) + 6$<br>

$T(n) = T(n-2) + 6 + 6$<br>

$T(n-2) = T(n-3) + 6$<br>
$T(n-3) = T(n-4) + 6$<br>
$T(n-4) = T(n-5) + 6$ when n > 1<br>

when n <= 1 but >= 0 then<br>
$T(0) = 3$<br>
$T(1) = 3$<br>
Because the base case for the function exits after 3 operations.<br>
But eventually we get to a number like T(2) after reducing (n) number of times<br>

$T(2) = T(1) + 6 ... + 6$<br>
$T(2) = 3 + 6 ... + 6$<br>
$T(3) = 3 + 6 + 6 ... + 6$<br>
So the pattern that emerges is the following:<br>
$T(n) = 3 + 6(n-1)$<br>
$T(n) = 3 + 6n - 6$<br>

$T(n) = 6n - 3$ for n > 1<br>
Therefore, T(n) is O(n) linear complexity for all values of n > 1.
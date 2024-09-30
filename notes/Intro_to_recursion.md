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
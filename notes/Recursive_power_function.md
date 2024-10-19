# Understanding Advanced Recursive Analysis and The Power Function

The power function is a function which takes a number, and finds it's power.<br>
This function can be diffcult to analyze.<br>

## Breaking Analysis Down

1. They all perform a certain number of constant operations before a recursive call
3. At the end of all recursive calls there is another certain number of operations which take place
4. Then we have 2 sets of constant operations
5. c1 which can represent constant operations during the function call
6. c2 which can represent constant operations when recursive calls hits a base case
7. n represents the total number of times recursion occurs, when solving
8. Thus a base generalized formula of T(n) = (c1 * n) + c2 can be used to analyze recursion

## Power Function and It's Recursion

```python
def power(base, n):
    if n == 0:
        return 1
    else:
        return base * power(base, n-1)
```

If anything is to the power of 0 it always equals 1 so thats our base case.<br>
When recursion reaches 0, it comes from n, n-1, n-2 ... 0.<br>
$B^n = base \cdot B^{n-1}$ becomes our recursion call formula.<br>
But this analyzes down to O(n) so linear complexity however, there is a function which is better.

## Better Power Function

```python
def power(base, n):
    if n == 0:                          # 1
        return 1                        # 1 when n = 0
    else:
        tmp = power(base, n//2)         # 1 + 1 + T(n/2)
        if n % 2 == 1:                  # 1 + 1
            return base * tmp * tmp     # 1 + 1 + 1
        else:
            return tmp * tmp            # assume we don't hit this
```

When the exponent is even, so (n=8), $power = b^4 \cdot b^4$<br>
The identity is that $b^n = b^{n/2} * b^{n/2}$ only when (n) is even<br>
When the exponent is odd we have the same formula but we also multiple that fomula by the base<br>
So $b^n = b^{n/2} * b^{n/2} * b$ when (n) is odd<br>
And it is this division of exponents during the function call which produces the faster runtime.

So the worst case for that function is the if statement nested inside the else, there the function does one extra operation. The function always performs 1 condition check before hitting the recursion so, during each recursive call it does 1 constant operation and calls recursively. The function's amount of recursive calls shrink by 2 everytime it gets called recursively so thats log(n) and then it performs a condition check.

$T(n) = 1 + T(n/2) + 2 + 2 + 3$<br>
$T(n) = T(n/2) + 8$<br>
Where $\frac{n}{1} + \frac{n}{2} ... + \frac{n}{n} + 0$<br>
Which is $2^0 + 2^1 + 2^2 + 2^3 ... + 2^{n-1}$<br>

And if we want to figure out how many times 2 to the power of (n) occurs we log.<br>
$log(n) = a$ where $n = b^a$ and we know that (a) is equal to (n-1)<br>
$log(n) = n-1$<br>
$n = log(n) + 1$<br>

$T(0) = 2$ and now we can start to put the whole expression together<br>
$T(n) = 8(log(n) + 1) + 2$<br>
$T(n) = 8log(n) + 8 + 2$<br>
$T(n) = 8log(n) + 10$<br>
Therefore, T(n) is O(log(n)) logarithmic time complexity.
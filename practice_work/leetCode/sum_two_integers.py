# Given two numbers (a) and (b) find their sum
# Without using the + or - operators, and return an int value


# Solution 01: Bit Manipulation Using Strings
# -------------------------------------------------------------------------------------------------------------------------
# Within code any arithmetic operation can be performed without using arithmetic operators by using bit manipulation
# Bit manipulation means making use of the bitWise operators AND, OR, XOR, NOT and Bit shifting
# We start with a mask of 1 which limits values to 32 bits, and then we start performing the addition process
# The addition process involves calculating the sum of bits using XOR while carrying over AND applying the mask using AND
# Then using 0x7FFFFFFF we see if (a) is positive if so we return (a) or else we add the mask and flip the bits
# This function has an average runtime of O(1) since the function performs fast hardware level operations
# -------------------------------------------------------------------------------------------------------------------------
def getSum(a, b):
    mask = 0xFFFFFFFF
    while b != 0:   # the carry value is b
        tmp = (a & b) << 1
        a = (a ^ b) & mask
        b = tmp & mask
    if a <= 0x7FFFFFFF:
        return a
    else:
        return ~(a ^ mask)
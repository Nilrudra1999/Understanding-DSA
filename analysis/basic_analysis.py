# The following functions were written either in Python, or another language and then converted over to Python
# These algorithms are more like simple functions than actual algorithms
# But they can be used to understand the fundementals of asymptotic analysis

# Function 01
def greet():
    print("Hello world!")

# Function 02
def apples(n):
    total = n * 5
    return total

# Function 03
def fruit(n):
    total = apples(n)
    return total

# Function 04
def adding(x):
    sum = 0
    n = (x*x)/2
    m = (x*x)/4
    for i in range(n):
        sum += 1
    for j in range(m):
        sum += 1
    for k in range(m+8):
        sum += 1
    return sum

# Function 05
def add_list(list):
    total = 0
    for i in range(len(list)):
        total += list[i]



# ****************************************************************************************
# The above basic functions are step 0 of the analysis where some code needs to be added.
# Next each function's operations will be counted within the md file and their 
# results as well as the results from timing experiments will be added.
# ****************************************************************************************

# Timing experiments --->
import time
import random

AMOUNT_OF_DATA = 100

# generate a list of unique random numbers (AMOUNT_OF_DATA unique values)
# my_list = random.sample(range(1, AMOUNT_OF_DATA*10), AMOUNT_OF_DATA)
total_time = 0

# Calling a function a certain number of times to measure time taken over all iterations
for i in range(AMOUNT_OF_DATA):
    start_time = time.perf_counter()
    result = greet()
    end_time = time.perf_counter()
    total_time = (end_time-start_time)
    print(f"Time for greet() = {total_time}")
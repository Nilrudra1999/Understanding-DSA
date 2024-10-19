# The following functions were written either in Python, or another language and then converted over to Python

# Function 1
def simple_loop(n):
    total = 0
    for i in range(2, n+3):
        total += i
    return total

# Function 2
def skip_loop(n):
    total = 0
    for i in range(1, n+1, 3):
        total += i
    return total

# Function 3
def nested_loop(n):
    total = 0
    for i in range(1, n+4):
        for j in range(1, i+2):
            total += j
    return total

# Function 4
def other_nested_loop(n):
    total = 0
    for i in range(1, n+4):
        for j in range(1, n+5):
            total += j
    return total



# The above iterative functions are step 0 of the analysis, adding some code
# Timing experiments code --->
import time

# generate a list of unique random numbers (AMOUNT_OF_DATA unique values)
# my_list = random.sample(range(1, AMOUNT_OF_DATA*10), AMOUNT_OF_DATA)
AMOUNT_OF_DATA = 100
total_time = 0

# Calling a function a certain number of times to measure time taken over all iterations
for i in range(AMOUNT_OF_DATA):
    start_time = time.perf_counter()
    result = nested_loop(i)
    end_time = time.perf_counter()
    total_time = (end_time-start_time)
    print(total_time)
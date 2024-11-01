# Given a list of numbers and a target number
# Find 2 numbers in the list which add up to the target and return their indices
# There is exactly 1 combo per list of numbers and solution worst solution = O(n^2)


# Solution 01: Brute Force
# -------------------------------------------------------------------------------------------------------------------------
# This algorithm is Linear search like, where (a) slides across (n) numbers in the list
# And (b) slides across (n - (a+1)) numbers in the list each time (a) slides by 1
# The time complexity is O(n^2) since each combination is checked, leading to n*n checks
# -------------------------------------------------------------------------------------------------------------------------
def two_sum01(nums, target):
    a = 0
    b = 1
    sum = nums[a] + nums[b]
    while sum != target:
        if b < len(nums)-1:
            b += 1
        else:
            a += 1
            b = a + 1
        sum = nums[a] + nums[b]
    return [a,b]


# Solution 02: Using a Hash Map
# -------------------------------------------------------------------------------------------------------------------------
# We are looking for combinations of numbers (a) and (b) such that T = a + b
# If a = nums[i] then for any index b = T - a, which is a possible value that can be found somewhere in the list
# The idea is to iterate through the list of numbers and find a value at some index thats equal to the difference (T - a)
# To find that value quickly, and also know the index associated with that value it's best to map it inside a Hash Map
# Since a Hash map provides search operations in O(1) time and key: value | value: index pair can be stored in it
# This means that longest operation runtime in this algorithm is the for-loop so the time complexity is O(n)
# -------------------------------------------------------------------------------------------------------------------------
def two_sum02(nums, target):
    num_map = {}    # value : index
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in num_map:
            return [num_map[diff], i]
        num_map[nums[i]] = i
    return None
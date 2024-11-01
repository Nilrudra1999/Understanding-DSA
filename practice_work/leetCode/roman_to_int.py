# Roman Numerials to Integers
# Given a string of Roman Numerials, find its value as an integer by adding the individual numerials
# There are special cases like IV = 4 instead of I=1 + V=5 = 6 so account for that



# Solution 01: Using a Hash Map to store Key:value pairs and KeyCombo:value pairs
# -------------------------------------------------------------------------------------------------------------------------
# This algorithm uses a Hash Table or python dictionary to map the Roman Numerials as keys to their values
# Every loop iteration the index[i] is checked and index[i+1] together to add the value of the KeyCombo iff they exist
# If not then only index[i] string "Key" is checked inside the Hash Map and the value associated is added to rc
# The space complexity is O(1) since no matter how big the length of the string got the Hash Map stays the same size
# The time complexity of this algorithm is O(n) since the loop runs for (n) iterations where n = len(str)
# -------------------------------------------------------------------------------------------------------------------------
def roman_to_int(str):
    roman_nums = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        "IV" : 4,
        "IX" : 9,
        "XL" : 40,
        "XC" : 90,
        "CD" : 400,
        "CM" : 900
    }
    rc = 0
    i = 0
    while i < len(str):
        if (i+1 < len(str)) and (str[i] + str[i+1]) in roman_nums:
            rc += roman_nums[str[i] + str[i+1]]
            i += 1
        elif str[i] in roman_nums:
            rc += roman_nums[str[i]]
        i += 1
    return rc
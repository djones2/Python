import sys

""" 
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(arr, target):
    result = [None, None]
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[i] + arr[j] == target:
                result[0] = i
                result[1] = j
                return result
            j += 1
        i += 1
        j = i + 1
    # If result is not found
    print("No solution found")
    return


# Main Program
if __name__ == "__main__":
    sampleArray1 = [11, 36, 3, 75]
    target = 111
    print("Array: " + str(sampleArray1))
    print("Target: " + str(target))
    result = twoSum(sampleArray1, target)
    print("Result: " + str(result))

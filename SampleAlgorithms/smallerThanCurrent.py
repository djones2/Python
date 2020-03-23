import sys

""" 
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
"""

def numSmallerThanThou(arr1):
    i = 0
    j = 0
    greaterCount = 0
    result = []
    while i < len(arr1):
        while j < len(arr1):
            if arr1[i] > arr1[j]:
                greaterCount += 1
            j += 1
        i += 1
        j = 0
        result.append(greaterCount)
        greaterCount = 0
    return result

# Main Program 
if __name__ == "__main__":
    sampleArray1 = [8,1,2,2,3]
    print("Array: " + str(sampleArray1))
    result = numSmallerThanThou(sampleArray1)
    print("Result: " + str(result))

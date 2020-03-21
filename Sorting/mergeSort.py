import sys

""" 
A quick example of performing merge sort on an array.
"""


def mergeSort(arr):
    print(str(arr))
    # Call merge on arrays bigger than 1 in length
    if len(arr) > 1:
        # Find midpoint
        middle = len(arr) // 2
        # Un-merge lists into two separate lists
        left = arr[:middle]
        right = arr[middle:]
        # Recursion to reduce list to single values
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print(str(arr))
    return arr


def getArray():
    # Grab length of array to initialize
    arrLen = input("Enter an array length: ")
    arr = [0] * arrLen
    i = 0
    # Enter in array values
    while i < len(arr):
        arr[i] = input("Enter array value: ")
        i += 1
    print("Array to sort: " + str(arr))
    # Return array
    return arr


# Main Program
if __name__ == "__main__":
    # Get input array
    toSort = getArray()
    # Call sorting algorithm
    sorted = mergeSort(toSort)

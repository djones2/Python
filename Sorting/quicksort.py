import sys

""" 
A quick example of performing merge sort on an array.
"""


def quicksort(arr, low, high):
    #
    if low < high:
        partitionIndex = partition(arr, low, high)
        quicksort(arr, low, partitionIndex - 1)
        quicksort(arr, partitionIndex + 1, high)
    return arr


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def getArray():
    # Grab length of array to initialize
    arrLen = input("Enter an array length: ")
    arr = [0] * int(arrLen)
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
    sorted = quicksort(toSort, 0, len(toSort) - 1)
    print(str(sorted))

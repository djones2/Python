import sys


""" 
A quick example of performing merge sort on an array.
"""

def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
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
            i+=1
            k+=1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1

    print(str(arr))

def getArray():
    arrLen = input("Enter an array length: ")
    arr = [0] * arrLen
    i = 0
    while i < len(arr):
        arr[i] = input("Enter array value: ")
        i += 1
    print("Array to sort: " + str(arr))
    return arr

# Main Program 
if __name__ == "__main__":
    toSort = getArray()
    mergeSort(toSort)
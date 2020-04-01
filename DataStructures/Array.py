import sys
import random

""" 
Array implementation. Only focused on integer usage.
Allowing use of Python system library for easier 
execution.
"""


class Array:
    def __init__(self, size):
        self.items = [0] * size

    def insert(self, data, index):
        return self.items.insert(index, data)

    def get(self, index):
        return self.items[index]
    
    def delete(self, index):
        self.items.pop(index)

    def sizeOfArray(self):
        return len(self.items)


# Main Program
if __name__ == "__main__":
    # Create Stack
    print("Creating array of size 10:")
    array = Array(10)
    sizeofarray = array.sizeOfArray()
    print("Size of array: " + str(sizeofarray))
    print("Inserting 3 into list at index 5:")
    array.insert(3, 5)
    print(str(array.items))
    print("Get that 3 from the list:")
    get = array.get(5)
    print(str(get))
    print("Deleting 3 from the list:")
    array.delete(5)
    print(str(array.items))
    
import sys

""" 
Linked list implementation.
"""

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ") 
            temp = temp.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Main Program
if __name__ == "__main__":
    # Create list
    linked_list = LinkedList()
    # Create some nodes
    linked_list.head = Node(21)
    second = Node(4)
    third = Node(3)
    # Populate linked list
    linked_list.head.next = second
    second.next = third
    # Print list contents
    linked_list.printLinkedList()
    print("")
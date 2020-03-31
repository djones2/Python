import sys
import random

""" 
Linked list implementation.
"""


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def delete(self, data):
        to_delete = Node(data)
        temp_node = self.head
        if self.head is not None:
            if (temp_node.data == to_delete.data):
                self.head = temp_node.next
                temp_node = None
                return

        # Iterate through nodes, see if data matches
        while (temp_node):
            if temp_node.data == to_delete.data:
                break
            # Hold previous Node
            prev = temp_node
            # Assign temp node to next node value
            temp_node = temp_node.next

        # Node not found, temp is none
        if (temp_node == None):
            return

        # Unlink found node from linked list
        prev.next = temp_node.next
        temp = None

    def search(self, target):
        temp_node = self.head
        while temp_node:
            if temp_node.data == target:
                return 1
            else:
                temp_node = temp_node.next
        return 0 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Main Program
if __name__ == "__main__":
    # Create list
    print("Creating linked list:")
    double_list = DoublyLinkedList()
    list_length = 10
    i = 0
    while (i < list_length):
        double_list.insert(random.randint(0, 10))
        i += 1
    # Print list contents
    double_list.printList()
    double_list.delete(8)
    double_list.printList()
    double_list.insert(8)
    double_list.printList()
    if double_list.search(4):
        print("Found " + str(4) + " in Linked List.")
    else:
        print("Could not find " + str(4) + " in Linked List.")

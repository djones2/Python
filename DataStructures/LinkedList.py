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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Main Program
if __name__ == "__main__":
    # Create list
    print("Creating linked list:")
    linked_list = LinkedList()
    # Create some nodes
    linked_list.insert(21)
    linked_list.insert(12)
    linked_list.insert(4)
    # Print list contents
    linked_list.printLinkedList()
    linked_list.delete(12)
    print("Deleting node from list:")
    linked_list.printLinkedList()

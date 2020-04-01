import sys
import random

""" 
Stack implementation.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        pop_index = len(self.items) - 1
        pop_value = self.items[len(self.items) - 1]
        self.items = self.items[:pop_index]
        return pop_value

    def isEmpty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[len(self.items) - 1]

# Main Program
if __name__ == "__main__":
    # Create Stack
    stack = Stack()
    # Check if it is empty
    print("Is the stack empty? -> " + str(stack.isEmpty()))
    i = 0
    print("Pushing 10 items to the stack:")
    while (i < 10):
        stack.push(random.randint(0, 10))
        i += 1
    print(str(stack.items))
    print("Popping value off of stack: " + str(stack.pop()))
    print("Current stack: ")
    print(str(stack.items))
    print("Is the stack empty? -> " + str(stack.isEmpty()))
    print("Here's the new top stack value: " + str(stack.top()))
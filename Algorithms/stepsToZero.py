import sys

""" 
Given an integer greater than 0, return the number of steps 
to reduce it to zero. 
If the current number is even, you have to divide it by 2. 
Otherwise, you have to subtract 1 from it.
Example:
Enter a value: 14
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
"""

def numberOfSteps(num, step):
    if num == 0:
        return
    elif (num % 2) == 1:
        print("Step " + str(step) + ") " + str(num) + " is odd; subtract 1 and obtain " 
            + str(num-1) + ".")
        step += 1
        return numberOfSteps(num - 1, step)
    else:
        print("Step " + str(step) + ") " + str(num) + " is even; divide by 2 and obtain " 
            + str(num / 2) + ".")
        step += 1
        return numberOfSteps(num / 2, step)

# Main Program 
if __name__ == "__main__":
    step = 1
    val = input("Enter a value: ")
    print("Explanation:")
    numberOfSteps(val, step)
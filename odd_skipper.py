# Program: Odd Number Skipper
# Author: [Akash Raval]
# Purpose: Demonstrates the use of 'break' and 'continue' in Loops

while True:
    # Continuously accept integer input from the user
    n = int(input('Enter number: '))

    # Exit Condition: If the user enters 0, stop the loop immediately
    if n == 0:
        print("Exiting program...")
        break

    # Check if the number is Even (Divisible by 2)
    if n % 2 == 0:
        # If it's Even, print the number
        print(f"Even Number: {n}")
    else:
        # If the number is Odd, skip the rest of the loop and start over
        continue

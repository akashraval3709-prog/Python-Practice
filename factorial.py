# Program: Factorial Calculator
# Author: Akash Raval
# Purpose: Calculates the factorial of a number (n!) using a for loop

n = int(input('Enter number: '))  # Take integer input from user
result = 1  # Initialize result to 1 (since multiplying by 0 would make it 0)

# Loop from 1 to n (we use n+1 because range stops one step before)
for i in range(1, n+1):
    result = result * i  # Multiply current number with the result

print(f'The Factorial of {n} is: {result}')

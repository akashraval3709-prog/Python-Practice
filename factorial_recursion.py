# Function to calculate factorial using Recursion
def factorial(n):
    # Base Case: If n is 0 or 1, stop recursion and return 1
    # Because 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive Case: Function calls itself with (n-1)
    # Formula: n * (n-1)!
    return n * factorial(n - 1)

# Main part of the program
# Take input from user and convert string to integer
n = int(input('Enter the number  : ')) 

# Call the function and store result in 'ans'
ans = factorial(n)

# Display the final output using f-string
print(f'Factorial {n} is {ans} ')

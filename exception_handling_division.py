# Program: Safe Division Calculator
# Author: Akash Raval
# Purpose: Demonstrate Exception Handling (try, except, else, finally)

try:
    # Attempting to take input and perform division
    num1 = int(input('Enter Number 1: '))
    num2 = int(input('Enter Number 2: '))
    
    ans = num1 / num2
    print(f"Result: {ans}")

except ValueError:
    # Executes if user enters text instead of numbers
    print('❌ Invalid Input! Please enter a valid integer number.')

except ZeroDivisionError:
    # Executes if user tries to divide by 0
    print('❌ Error: Cannot divide by Zero (0). Please use a valid Number 2.')

except Exception as e:
    # Executes for any other unknown errors
    print(f'❌ An unexpected error occurred: {e}')

else:
    # Executes ONLY if NO error occurs
    print('✅ Division Successful!')

finally:
    # Executes ALWAYS (whether error happens or not)
    print('🔄 Task Completed.')

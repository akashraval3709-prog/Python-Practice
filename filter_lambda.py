# Program: Filter Even Numbers using Lambda
# Author: Akash Raval
# Purpose: Use filter() and lambda function to extract even numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Logic: filter(function, iterable)
# lambda x: x % 2 == 0 checks if a number is even
# list() converts the filter object back to a list
new_list = list(filter(lambda x: x % 2 == 0, nums))

print(f"Original List: {nums}")
print(f"Filtered List: {new_list}")

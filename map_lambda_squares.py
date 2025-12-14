# Program: Square Numbers using Map & Lambda
# Author: Akash Raval
# Purpose: Transform a list by squaring each number using map() function

nums = [1, 2, 3, 4, 5]

# Logic: map(function, iterable)
# 'map' applies the lambda function (x*x) to EVERY item in the list
square_list = list(map(lambda x: x*x, nums))

print(f"Original List: {nums}")
print(f"Squared List : {square_list}")

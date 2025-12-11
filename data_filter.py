# Program: Positive & Negative Number Separator
# Author: Akash Raval
# Purpose: Filter data by separating positive and negative integers into different lists

# Input List containing mixed numbers
data = [10, -5, 20, -2, 0, -10, 45, -3]

# Initialize empty lists to store separated values
negative = []
positive = []

# Loop through each item in the data list
for item in data:
    # Logic: Check if the number is less than 0
    if item < 0:
        negative.append(item)  # Add to negative list
    else:
        positive.append(item)  # Add to positive list (includes 0)

# Display the results
print(f'Original Data : {data}')
print(f'Positive List : {positive}')
print(f'Negative List : {negative}')

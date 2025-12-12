# Program: Subject Marks Total Calculator
# Author: Akash Raval
# Purpose: Calculate total marks by adding elements from two different lists using index

# Two lists representing marks of two subjects
maths = [40, 50, 60]
science = [10, 20, 30]

# Empty list to store the total
total_marks = []

# Loop through the length of the list (assuming both lists have same size)
for i in range(len(maths)):
    # Logic: Access elements from both lists using the same index 'i'
    m = maths[i]
    s = science[i]
    
    # Add them and append to the new list
    total_marks.append(m + s)

print(f'Maths Marks   : {maths}')
print(f'Science Marks : {science}')
print('---------------------------')
print(f'Total Marks   : {total_marks}')

# Program: Character Frequency Counter
# Author: Akash Raval
# Purpose: Count how many times each character appears in a string using a Dictionary

d = {} # Create an empty dictionary

# Take input from the user
grand_word = input("Enter a word/string: ")

# Loop through each character in the string
for char in grand_word:
    # Check if character is already in dictionary
    if char in d:
        # If yes, increase the count by 1
        d[char] = d[char] + 1
    else:
        # If no, add it to dictionary with count 1
        d[char] = 1 
        
print("Character Frequency:", d)

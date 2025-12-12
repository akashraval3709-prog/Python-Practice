# Program: Word Splitter and Joiner
# Author: Akash Raval
# Purpose: Demonstrate string manipulation using split() and join() methods

# Step 1: Take input from the user
text = input('Enter your sentence: ')

# Step 2: Split the sentence into a list of words
# The split() method breaks the string whenever it finds a space
word_list = text.split()

print(f'\nList of Words: {word_list}')
print(f'Total Word Count: {len(word_list)}')

# Step 3: Join the list back into a single sentence
# The join() method combines list items using a separator (here, a space " ")
rejoined_sentence = " ".join(word_list)

print(f'Rejoined Sentence: {rejoined_sentence}')

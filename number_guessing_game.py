
# Program: Number Guessing Game
# Author: [Akash Raval]
# Purpose: A fun game where the user tries to guess a randomly generated number
import random  # Import the random module to generate random numbers
# [cite_start]Generate a random secret number between 1 and 100 [cite: 871, 872]
select_number = random.randint(1, 100)

# [cite_start]Start an infinite loop to keep asking for guesses until the user wins [cite: 447]
while True:
    # Take integer input from user [cite: 144]
    guess = int(input('enter the number : '))
# [cite_start]Check if the user's guess matches the secret number [cite: 369]
    if guess == select_number:
        print('You Won!')
        break
    # [cite_start]Provide a hint if the guess is lower than the actual number [cite: 874]
    elif guess < select_number:
        print('Too Low!Try Higher')
        # [cite_start]Provide a hint if the guess is higher than the actual number [cite: 873]
    elif guess > select_number:
        print('Too High!Try Lower')

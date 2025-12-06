
# Program: Secure Login System with 3 Attempts
# Author: [Your Name]
# Purpose: Basic password authentication logic for Cyber Security

# Store the correct password
password = "python123"

# Loop to allow a maximum of 3 attempts
for i in range(3):
    # Prompt the user to enter the password
    pin = input('\nenyter your password : ')
# Validate the entered password
    if pin == password:
        print('Access Granted')
        break  # Break the loop if authentication is successful
    else:
        # Check if it was the last attempt
        if i != 2:
            print('your password is wrong pleas try again........')
        # Lock the system after 3 failed attempts
        else:
            print('SYSTEM LOCKED')

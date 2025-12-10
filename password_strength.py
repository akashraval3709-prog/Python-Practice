# Program: Password Strength Checker
# Author: Akash Raval
# Purpose: Validate password complexity based on length, digits, and special characters

def check_password_strength(password):
    # Rule 1: Check Length (Must be at least 8 characters)
    if len(password) < 8:
        return 'Weak'
    
    # Rule 2: Check for Digits (0-9)
    has_digit = False
    for char in password:
        if char in '1234567890':
            has_digit = True
            break
            
    if not has_digit:
        return 'Medium'
    
    # Rule 3: Check for Special Characters
    has_special = False
    for char in password:
        if char in '@#$-_':
            has_special = True
            break
            
    if not has_special:
        return 'Medium'
    
    # If all conditions are met
    return 'Strong'

# Main execution
user_pass = input('Enter your password: ')
strength = check_password_strength(user_pass)

print(f'Your password strength is: {strength}')

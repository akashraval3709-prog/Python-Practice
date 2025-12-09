# Program: Basic Encryption Tool (Caesar Cipher)
# Author: Akash Raval
# Purpose: Encrypt a message by shifting ASCII characters based on a user key

message = input('Enter your message: ')
key = int(input('Enter your shift key: '))  # The "Secret Key" for encryption

print("Encrypted Message: ", end="")

for char in message:
    # Logic: Get ASCII value -> Add Key -> Convert back to Character
    ascii_val = ord(char)
    encrypted_char = chr(ascii_val + key)
    
    # Print character by character on the same line
    print(encrypted_char, end="")

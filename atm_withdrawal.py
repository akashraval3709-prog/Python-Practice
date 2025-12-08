
# Program: ATM Withdrawal Logic
# Author: Akash Raval
# Purpose: Secure withdrawal system using Nested If-Else conditions
# Initial account details
current_balance = 10000
correct_pin = 1234

print("--- Welcome to Python ATM ---")
# Step 1: Security Check (PIN Verification)
entered_pin = int(input('Enter your PIN: '))

if entered_pin == correct_pin:
    # Step 2: Withdrawal Request
    withdraw_amount = int(input("Enter amount to withdraw: "))

    # Nested Check: Validate sufficient funds
    if withdraw_amount <= current_balance:
        remaining_balance = current_balance - withdraw_amount
        print("Transaction Successful!✅")
        print(f"Remaining Balance is: {remaining_balance}")
    else:
        print("Transaction Failed: Insufficient Balance ❌") 
else:
    print("Access Denied: Wrong PIN 🚫")
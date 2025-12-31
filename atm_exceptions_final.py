

# Project: ATM System with Full Exception Handling
# Author: Akash Raval

# 1. Defining Custom Exceptions
class InvalidAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class DailyLimitExceededError(Exception):
    pass

class AmountEmptyError(Exception):
    pass

# Global Data
balance = 100000
daily_limit = 5000

print('\n' + '='*40)
print(' 🏧 WELCOME TO PYTHON BANK 🏧')
print('='*40)

try:
    user_input = input('👉 Enter Amount: ')

    # Check 1: Empty Input
    # .strip() removes spaces. If input is empty, raise Error.
    if not user_input.strip():
        raise AmountEmptyError("🚫 Alert: Amount cannot be empty!")

    amount = int(user_input)

    # Check 2: Negative Amount
    if amount <= 0:
        raise InvalidAmountError('🚫 Alert: Amount must be positive.')

    # Check 3: Insufficient Balance
    if amount > balance:
        raise InsufficientBalanceError('❌ Transaction Failed: Check your balance.')

    # Check 4: Daily Limit
    if amount > daily_limit:
        raise DailyLimitExceededError('⚠️ Alert: Daily Limit (5000) Exceeded.')

    # If all checks pass, perform transaction
    balance -= amount
    print(f"\n✅ Please collect your cash: ₹{amount}")
    print(f"💰 Remaining Balance: ₹{balance}")

# Handling All Exceptions
except AmountEmptyError as e:
    print(e)

except InvalidAmountError as e:
    print(e)

except InsufficientBalanceError as e:
    print(e)

except DailyLimitExceededError as e:
    print(e)

except ValueError:
    print("🚫 Alert: Please enter numbers only!")

except Exception as e:
    print(f"❌ Unknown Error: {e}")

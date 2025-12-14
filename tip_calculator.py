# Program: Tip Calculator & Bill Splitter
# Author: Akash Raval
# Purpose: Calculate tip, total bill, and split amount per person

# Input Section
bill = float(input('\nEnter your bill amount: '))
tip = float(input('Enter tip percentage (10, 12, 15): '))
people = int(input('How many people to split the bill: '))

# Calculation Logic
tip_amount = bill * tip / 100
total_bill = bill + tip_amount
per_person = total_bill / people

# Output Section (Receipt Design)
print('\n' + '-'*35)
print(f'Bill Amount      : {bill:.2f}')
print(f'Tip Amount       : {tip_amount:.2f}')
print(f'Total to Pay     : {total_bill:.2f}')  # Added .2f for currency format
print('-'*35)
print(f'Per Person Share : {per_person:.2f}') # Logic is perfect!
print('-'*35)

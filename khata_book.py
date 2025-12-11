# Program: Digital Khata Book
# Author: Akash Raval
# Purpose: Manage daily expenses using Python Dictionary (Key-Value pairs)

print("\t\t--- Welcome to Khata Book ---")

# Initialize an empty dictionary to store data
khata_book = {} 
total = 0

# Start an infinite loop to add items
while True:
    item = input('Enter the item (or type "stop"/"done" to exit): ') # Take input from user 
    
    # Exit condition: Stop the loop if user types stop or done
    if item == 'stop' or item == 'done':
        break
    
    # Take price input
    price = int(input('Enter price: '))

    # Logic: Store item as 'Key' and price as 'Value' in dictionary
    khata_book[item] = price

# Print the Final Bill
print("\n\t\t--- Final Bill ---")
print("ITEM\t\tPRICE") # Header for the bill

# Loop through the dictionary to print items and prices
for k, v in khata_book.items():
    print(f'{k}\t\t{v}')    

print('________________________')

# Calculate total sum using values
for p in khata_book.values():
    total = total + p
    
print(f'FINAL TOTAL : {total}')

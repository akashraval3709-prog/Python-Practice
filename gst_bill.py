
# Program: GST Bill Calculator 
# Author: Akash Raval
# Purpose: Calculate total amount with 18% GST using List and Sum function

# List of item prices
prices = [40, 50, 70, 55, 45]

# Calculate total using sum() function
total = sum(prices)

# Calculate 18% GST and round it to 2 decimal places
gst = round(total * 0.18, 2)

# Calculate final amount
famount = total + gst

# Print the Bill
print(f'SUBTOTAL     : {total}')
print(f'GST (18%)    : {gst}')
print('-----------------------')
print(f'FINAL AMOUNT : {famount}')

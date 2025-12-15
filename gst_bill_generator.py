# Program: GST Bill Generator
# Author: Akash Raval
# Purpose: Calculate 18% GST and generate a final bill using Functions

def calculate_gst(amount):
    """Function to calculate 18% GST"""
    tax = amount * 0.18
    return tax

# Main Input
try:
    bill_amount = float(input('👉 Enter your Bill Amount: '))

    # Calling the function
    gst_amount = calculate_gst(bill_amount)
    final_bill = bill_amount + gst_amount

    # Printing the Receipt
    print('\n\t\t 🏩 TAX INVOICE 🏩')
    print('='*35)
    print(f'Base Amount \t:  {bill_amount:.2f}')
    print(f'GST (18%)   \t: +{gst_amount:.2f}')
    print('-'*35)
    print(f'GRAND TOTAL \t:  {final_bill:.2f}')
    print('='*35)

except ValueError:
    print("❌ Error: Please enter a valid number.")

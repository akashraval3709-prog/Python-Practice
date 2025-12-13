# Program: Smart Khata Book System
# Author: Akash Raval
# Purpose: Manage credits and debits using Dictionary with a clean English Menu

khata = {}  # Dictionary name kept as 'khata'

while True:
    # Improved Menu Design (English Only)
    print("\n" + "="*40)
    print("      🛒 SMART KHATA BOOK SYSTEM")
    print("="*40)
    print("  1. Add Credit (Udhar)")
    print("  2. View Customer Balance")
    print("  3. Settle Payment (Jama)")
    print("  4. Show All Accounts")
    print("  5. Exit System")
    print("-" * 40)
    
    # Changed 'choice' to 'menu_choice'
    menu_choice = int(input('👉 Enter your choice key: '))

    if menu_choice == 1:
        # Changed 'name' to 'customer_name'
        customer_name = input('Enter customer name: ')
        # Changed 'amount' to 'credit_amount'
        credit_amount = int(input('Enter credit amount: '))

        # Logic Fix: Check if customer exists in khata dictionary
        if customer_name in khata:
            total = khata[customer_name] + credit_amount
            khata[customer_name] = total
            print(f"✅ Amount added! New Balance: {khata[customer_name]}")
        else:
            khata[customer_name] = credit_amount
            print(f"✅ New Account Created for {customer_name}")

    elif menu_choice == 2:
        # Changed 'cust_name' to 'search_name'
        search_name = input('Enter customer name to search: ')
        # Uses .get() to avoid errors if name doesn't exist
        print(f'\n👤 Customer: {search_name} | 💰 Due Amount: {khata.get(search_name, "Not Found")}')

    elif menu_choice == 3:
        # Changed 'custo_name' to 'payer_name'
        payer_name = input('Enter customer name for payment: ')
        # Changed 'payment' to 'payment_amount'
        payment_amount = int(input('Enter payment amount: '))

        if payer_name in khata:
            khata[payer_name] = khata[payer_name] - payment_amount
            print(f"✅ Payment Successful! Remaining Due: {khata[payer_name]}")
        else:
            print("❌ Customer not found!")

    elif menu_choice == 4:
        print('\n\t--- 📜 Total Calculation ---')
        print("Customer\tBalance")
        print("-" * 25)
        # Changed 'k, v' to 'customer, balance' for better readability
        for customer, balance in khata.items():
            print(f'{customer}\t\t{balance}')
            
    elif menu_choice == 5:
        print("Saving data... Exiting. Have a nice day! 👋")
        break
        
    else:
        print("❌ Invalid input! Please select 1-5.")


current_balance = 5000


def deposit_money(amount):
    """Function to add money to the account"""
    global current_balance
    current_balance += amount
    print(f"\n✅ Successfully Deposited: ₹{amount}")
    print(f"💰 New Balance: ₹{current_balance}")


def withdraw_money(amount):
    """Function to withdraw money with validation"""
    global current_balance
    if amount <= current_balance:
        current_balance -= amount
        print(f"\n✅ Withdrawal Successful: ₹{amount}")
        print(f"💰 Remaining Balance: ₹{current_balance}")
    else:
        print(f"\n❌ Transaction Failed! Insufficient Balance.")
        print(f"⚠️ Your Balance is only: ₹{current_balance}")


def check_balance():
    """Function to display current balance"""
    print('\n' + '-'*30)
    print(f' 🏦 Available Balance: ₹{current_balance}')
    print('-'*30)


# Main Menu Loop
while True:
    print('\n' + '='*30)
    print('      🏧 MINI ATM SYSTEM      ')
    print('='*30)
    print('  1. Deposit Cash 💵')
    print('  2. Withdraw Cash 💳')
    print('  3. Check Balance 🧮')
    print('  4. Exit 🚫')
    print('-'*30)

    menu_choice = int(input('👉 Enter your choice: '))

    if menu_choice == 1:
        amount = int(input('\nEnter amount to Deposit: ₹'))
        deposit_money(amount)

    elif menu_choice == 2:
        amount = int(input('\nEnter amount to Withdraw: ₹'))
        withdraw_money(amount)

    elif menu_choice == 3:
        check_balance()

    elif menu_choice == 4:
        print("\n👋 Thank you for using Mini ATM. Have a nice day!")
        break
    else:
        print("\n❌ Invalid Choice! Please select 1-4.")

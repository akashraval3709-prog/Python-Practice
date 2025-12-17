# Project: Contact Management System
# Author: Akash Raval
# Purpose: Create, Read, Delete, and View contacts using Python Dictionary

# Global Dictionary to store data
contacts = {}

def add_contact(name, number):
    """Function to add a new contact"""
    contacts[name] = number
    print(f"✅ Contact Saved: {name} -> {number}")

def search_contact(name):
    """Function to search for a contact"""
    print('\n' + '-'*30)
    # .get() returns None if key is not found, preventing errors
    number = contacts.get(name)
    
    if number:
        print(f"🔍 Found: {name} \t 📞 {number}")
    else:
        print(f"🚫 Sorry, '{name}' not found in contact book.")
    print('-'*30)

def delete_contact(name):
    """Function to delete a contact"""
    if name in contacts:   
        contacts.pop(name)
        print(f"🗑️ Contact '{name}' deleted successfully.")
    else:
        print(f"🚫 Cannot Delete: '{name}' not found.")

def view_all():
    """Function to display all contacts"""
    print('\n' + '='*30)
    print(" 📖 YOUR CONTACT LIST 📖")
    print('='*30)
    
    if not contacts:
        print("📂 Contact book is empty!")
    else:
        for name, num in contacts.items():
            print(f"👤 {name} \t 📞 {num}")
            print('-'*30)

# Main Menu Loop
while True:
    print('\n' + '='*30)
    print('    📞 CONTACT MANAGER 📞')
    print('='*30)
    print('1. 👉 Add New Contact')
    print('2. 👉 Search Contact')
    print('3. 👉 Delete Contact')
    print('4. 👉 View All Contacts')
    print('5. 👉 Exit')
    print('-'*30)

    try:
        menu_choice = int(input('Enter Your Choice (1-5): '))

        if menu_choice == 1:
            name = input('Enter Name: ').title() # .title() makes first letter capital
            num = input('Enter Phone Number: ')
            add_contact(name, num)

        elif menu_choice == 2:
            name = input('Enter Name to Search: ').title()
            search_contact(name)

        elif menu_choice == 3:
            name = input('Enter Name to Delete: ').title()
            delete_contact(name)

        elif menu_choice == 4:
            view_all()

        elif menu_choice == 5:
            print("👋 Exiting... Have a nice day!")
            break
        
        else:
            print("❌ Invalid Choice! Please enter 1 to 5.")

    except ValueError:
        print("❌ Error: Please enter a valid number.")

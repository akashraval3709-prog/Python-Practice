# Program: Simple To-Do List Manager
# Author: Akash Raval
# Purpose: Manage daily tasks using List operations (Add, View, Exit)

# Define an empty list to store tasks
task_list = []

print("\t\t--- Welcome to Task Manager ---")

while True:  # Infinite loop to keep the menu active
    # Menu for user choice
    print('\n\t\t....MENU....')
    print('1. Add Task')
    print('2. Show Tasks')
    print('3. Exit')
    
    # Take integer input from user
    key = int(input('\nEnter your choice (1-3): '))

    if key == 1:  # Logic to ADD a task
        add = input('Enter your Task: ') 
        task_list.append(add)  # Add new task to the end of the list
        print(f'Task "{add}" added successfully!')

    elif key == 2:  # Logic to SHOW all tasks
        print('\n--- YOUR PENDING TASKS ---')
        # Check if list is empty
        if not task_list:
            print("No tasks found. Add some tasks first!")
        else:
            # Loop through each item in the task_list
            # enumerate() helps to show numbers (1, 2, 3...)
            for i, item in enumerate(task_list, 1):
                print(f'{i}. {item}') 

    elif key == 3:  # Logic to EXIT
        print('Exiting Task Manager. Have a productive day!')
        break
        
    else:
        print("Invalid choice, please select 1, 2, or 3.")

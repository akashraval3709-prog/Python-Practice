if __name__ == '__main__':
    # Step 1: Read the integer N (Total number of commands)
    # .strip() removes any leading/trailing whitespace
    N = int(input().strip())
    
    # Initialize an empty list to perform operations
    L = []

    # Step 2: Iterate N times to process each command
    for _ in range(N):
        # Read the input line, strip spaces, and split into a list of strings
        # Example input: "insert 0 5" -> cmd becomes ['insert', '0', '5']
        cmd = input().strip().split()
        
        # The first element is always the operation name (e.g., 'insert', 'print')
        op = cmd[0]

        # Check which operation to perform
        if op == 'insert':
            # insert(index, value): Adds value at the specified index
            # Convert strings to integers before passing to the function
            L.insert(int(cmd[1]), int(cmd[2]))
            
        elif op == 'print':
            # Display the current state of the list
            print(L)
            
        elif op == 'remove':
            # remove(value): Removes the first occurrence of the specified value
            L.remove(int(cmd[1]))
            
        elif op == 'append':
            # append(value): Adds the value to the end of the list
            L.append(int(cmd[1]))
            
        elif op == 'sort':
            # Sorts the list in ascending order
            L.sort()
            
        elif op == 'pop':
            # Removes the last element from the list
            # Added a check 'if L' to prevent error if list is empty
            if L:
                L.pop()
                
        elif op == 'reverse':
            # Reverses the order of elements in the list
            L.reverse()

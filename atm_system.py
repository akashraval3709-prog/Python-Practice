balance = 1000

while True:
    print(' MENU ')
    print('1 for Check Balace')
    print('2 for Deposit Balace')
    print('3 for withdraw Balace')
    print('4 for exit')

    x = int(input('Enter yor choice : '))

    if x == 1:
        print('Your balance is : ', balance)

    elif x == 2:
        add_balace = int(input('How to deposit balance enter :'))
        balance = balance + add_balace

    elif x == 3:
        with_draw = int(input('How to withdraw balance enter : '))
        if with_draw > balance:
            print('balance is not available :')

        else:
            balance = balance - with_draw
    elif x == 4:
        print('Thank you using Python ATM. Bye!')
        break

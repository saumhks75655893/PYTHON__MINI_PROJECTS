# WE ARE GOING TO MAKE A SIMPLE CALCULATOR : -------------
while True:
    choice = int(input('''
    1 Start calculator  
    2 Close calculator || Exit

    Enter the choice   : '''))

    if choice == 1:

        num1 = int(input("Enter the first number(1) : "))
        num2 = int(input("Enter the second number(2) : "))
        userInput = input(
            '''
            + 
            - 
            * 
            /
            Enter you choice among these ( + - * /) ==> '''
        )

        if (userInput == '+'):
            print("The Addition is  : ", num1 + num2)

        elif (userInput == "-"):
            print("The Substraction of the numbers is   :", num1 - num2)

        elif (userInput == "*"):
            print("Multiplication of the numbers is   :", num1 * num2)

        elif (userInput == "/"):
            print("The Devision of the numbers is   :",num1 / num2)
    
    if choice == 2:
        print("The user want to close the close calculator ....")
        print("Calculator Closed....")
        break

    else:
        print("Invalid choice. . . . ")





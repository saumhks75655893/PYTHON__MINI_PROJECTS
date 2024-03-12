#          ----------------------- : Bank Operation using OOPS : ------------------------                  #
class Bank:
    bankName = "Bank Of Baroda"
    branch = "Dharde"

    #  Create Account

    def __init__(self, username, panNo, address):
        self.username = username
        self.panNo = panNo
        self.address = address
        self.balance = 0.0
        print(
            f"Congratulation ! {self.username}, Your account created successfully.")
        print("*"*80)
        
    # DEPOSITE

    def deposite(self, amount):
        self.balance += amount
        print("*"*80)
        print(f"{amount} deposited succussfully.....")
        print("*"*80)

    # WITHDRAW

    def withdraw(self, amount):
        if (amount < self.balance):
            self.balance -= amount
            print("*"*80)
            print(f"{amount} is withdrawn successfully ... ")
            print("*"*80)
        else:
            print("Insufficient amount ... ")

    # MINI STATEMENT 

    def miniStatement(self):
        print("*"*80)
        print("Name : ",self.username, "       |       "  ,    "PAN CARD Number : ",self.panNo)
        print("Addres is          |          ",self.address)
        print("Your Account Balance is : ",self.balance)
        print("*"*80)


# ACCOUNT OPENING DETAILS
# Acount Holder Details
print("\n\n")
print(f"Welcome to {Bank.bankName} , branch {Bank.branch}.")
print("*" * 80)
username = input("Enter Your Name : ")
pan = input("Enter PAN card Number : ")
address = input("Enter Your Address : ")
print("*"*80)

p1 = Bank(username, pan, address)

while True:
    print("Please select a option ... ")
    print('''
        1. Deposite 
        2. Withdraw 
        3. MiniStatement 
        4. Exit
    ''')

    option = int(input("Enter you  choice : "))

    if option == 1:
        amount = float(input("Enter the amount to Deposite : "))
        p1.deposite(amount)

    if option == 2:
        amount = float(input("Enter the withdraw amount : "))
        p1.withdraw(amount)

    if option == 3: 
        p1.miniStatement()

    if option == 4:
        print("\n")
        print("*"*80)
        print(f"Thanks for using {p1.bankName}")
        print("*"*80)
        print("\n")
        break

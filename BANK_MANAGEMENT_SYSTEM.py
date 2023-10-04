import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='Mysql@75655893#',
                               database='bank_management'
                               )



def OpenAcc():
    n = input("Enter The  Name : ")
    ac = input("Enter the Account Number : ")
    db = input("Enter the Date of birth : ")
    add = input("Enter The Address  :  ")
    cn = input("Enter The Contact Number : ")
    ob = int(input("Enter The Opening Balance "))
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = ('insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values(%s,%s,%s)')
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Data Entered Successfullyy ....... ")
    main()


def DepositAmount():
    amount = int(input("Enter the amount , You want to deposite  :  "))
    ac = input("Enter the Account Number : ")
    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] + amount
    sql = ('update amount set balance where AccNo = %s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()


def WithdrawAmount():

    amount = int(input("Enter the amount , You want to deposite  :  "))
    ac = input("Enter the Account Number : ")
    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update amount set balance where AccNo = %s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()


def BalanceEnquiry():
    ac = input("Enter the account No  :  ")
    a = 'select * from amount where AccNo = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("Balance for account : ", ac, " is ", result[-1])
    main()


def CustomerDetails():

    ac = input("Enter the account no  :  ")
    a = 'select * from account where AccNo = %s'
    data = (ac, )
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)

    main()


def CloseAccount():
    ac = input("Enter the Account Number : ")
    sql1 = 'delete from account where AccNo=%s'
    sql2 = 'delete from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()


def main():

    print('''
            1. OPEN NEW ACCOUNT
            2. DEPOSITE AMOUNT 
            3. WITHDRAW AMOUNT
            4. BALANCE ENQUIRY
            5. DISPLAY CUSTOMER DETAILS
            6. CLOSE AN ACCOUNT
            ''')

    choice = int(input("Enter The Task You Want To Perform :  "))
    if (choice == 1):
        OpenAcc()
    elif (choice == 2):
        DepositAmount()

    elif (choice == 3):
        WithdrawAmount()
    elif (choice == 4):
        BalanceEnquiry()
    elif (choice == 5):
        CustomerDetails()

    elif (choice == 6):
        CloseAccount()

    else:
        print("Invalid Choice   .....  ")


main()

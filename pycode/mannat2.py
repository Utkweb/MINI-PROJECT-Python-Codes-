import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="",
    database = 'bank_management'
    )

# Check if the connection is successful
cur = conn.cursor(buffered=True) 

def OpenAcc():
    name = input('Enter your name: ')
    acc_no = input('Enter your account number: ')
    DOB = input('Enter your date of birth: ')
    address = input('Enter your address: ')
    contact_no = input('Enter your phone number: ')
    opening_bal = int(input('Enter your opening balance: '))

    # Values for the 'account' table
    account_values = (name, acc_no, DOB, address, contact_no, opening_bal)
    account_query = ("INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s)")

    # Values for the 'amount' table
    amount_values = (acc_no, name, opening_bal)
    amount_query = ("INSERT INTO amount VALUES (%s, %s, %s)")

    cur = conn.cursor()
    cur.execute(account_query, account_values)
    cur.execute(amount_query, amount_values)
    conn.commit()
    print('Account opened successfully!')
    main()



def DepositAmt():
    amount = int(input('Enter the amount you want to deposit: '))
    acc_no = input('Enter your account number: ')

    amount_query = ("select balance from ammount where account_no = %s")
    d1 = (acc_no,)
    cur = conn.cursor()
    cur.execute(amount_query, d1)
    result = cur.fetchone()
    t = result[0] + amount

    update_query = (" update amount set balance where account_no = %s")
    d2 = (t, acc_no)
    cur.execute(update_query, d2)
    conn.commit()
    main()

def WithdrawAmt():
    amount = int(input('Enter the amount you want to deposit: '))
    acc_no = input('Enter your account number: ')

    amount_query = ("select balance from amount where account_no = %s")
    d1 = (acc_no,)
    cur = conn.cursor()
    cur.execute(amount_query, d1)
    result = cur.fetchone()
    t = result[0] - amount

    update_query = (" update amount set balance where account_no = %s")
    d2 = (t, acc_no)
    cur.execute(update_query, d2)
    conn.commit()
    main()


def Balance():
    account = input('Ebter your account number: ')
    balance_query = ('select balance from amount where account_no = %s')
    d1 = (account,)
    cur = conn.cursor()
    cur.execute(balance_query, d1)
    result = cur.fetchone()
    print('Your balance for account :',account, 'is', result[-1])
    main()


def display_details ():
    account = input("Enter your account number: ")
    display_query = ('select * from account where account_no = %s')
    d1 = (account,)
    cur = conn.cursor()
    cur.execute(display_query, d1)
    result = cur.fetchone()
    for i in result:
        print(i)
    main() 

def CloseAcc():
    acc_no = input("Enter your account number" )
    delete_query = ('DELETE FROM account WHERE account_no = %s')
    d1 = (acc_no,)
    delete2_query = ('DELETE FROM amount WHERE account_no = %s')
    cur = conn.cursor()
    cur.execute(delete_query, d1)
    cur.execute(delete2_query, d1)
    conn.commit()
    print('Your account has been deleted')
    main()

def main():
    print('''
    1. Open Account
    2. Deposit Amount
    3. Withdraw Amount
    4. View Balance 
    5. Customer details 
    6. Close an account''')
    choice = int(input('What action would you like to complete? / For exit press 0 '))

    if choice == 1:
        OpenAcc()
    elif choice == 2:
        DepositAmt()
    elif choice == 3:
        WithdrawAmt()
    elif choice == 4:
        Balance()
    elif choice == 5:
        display_details()
    elif choice == 6:
        CloseAcc()
    else:
        print('Thank you for using our service')

main()
import cx_Oracle

def address_change(accountNumber):
    print(type(accountNumber))
    new_addr=raw_input("Enter the new Address : ")
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    cur.execute("update detail set address=:1 where accountnumber=:2",(new_addr,accountNumber))
    con.commit()
    con.close()
    return 0

def money_deposit(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    credit=input("enter money to deposit")
    cur.execute("update detail set money=money + :1 where accountnumber=:2",(credit,accountNumber))
    con.commit()
    con.close()


def money_withdraw(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    debit=input("enter money to withdraw")
    cur.execute("update detail set money=money - :1 where accountnumber=:2",(debit,accountNumber))
    con.commit()
    con.close()

def print_statement():
    pass

def money_transfer():
    pass

def account_closure():
    pass

def customer_logout():
    pass

def subMenu(accountNumber):
    print("Menu\n1.address_change\n2.money_deposit\n3.money_withdraw\n4.print_statement\n5.money_transfer")
    print("6.account_closure\n7.customer_logout")
    num=input("Choose the action:")
    if(num==1):
        address_change(accountNumber)
    elif(num==2):
        money_deposit(accountNumber)
    elif(num==3):
        money_withdraw(accountNumber)
    elif(num==4):
        print_statement(accountNumber)
    elif(num==5):
        money_transfer
    elif(num==6):
        account_closure
    elif(num==7):
        customer_logout

import cx_Oracle
import time
from tabulate import tabulate

def address_change(accountNumber):
    print(type(accountNumber))
    new_addr=raw_input("Enter the new Address : ")
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    cur.execute("update detail set address=:1 where accountnumber=:2",(new_addr,accountNumber))
    con.commit()
    con.close()
    subMenu(accountNumber)

def money_deposit(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    credit=input("enter money to deposit")
    cur.execute("update detail set money=money + :1 where accountnumber=:2",(credit,accountNumber))
    cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
    balance=cur.fetchall()
    account=str(accountNumber)
    account="b_"+account
    date=time.strftime("%x")
    query="Insert into "+ account + " VALUES (:1,:2,:3,:4)"
    cur.execute(query,(date,'credit',credit,balance[0][0]))
    con.commit()
    con.close()
    subMenu(accountNumber)


def money_withdraw(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    debit=input("enter money to withdraw")
    cur.execute("update detail set money=money - :1 where accountnumber=:2",(debit,accountNumber))
    cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
    balance=cur.fetchall()
    account=str(accountNumber)
    account="b_"+account
    date=time.strftime("%x")
    query="Insert into "+ account + " VALUES (:1,:2,:3,:4)"
    cur.execute(query,(date,'debit',debit,balance[0][0]))
    con.commit()
    con.close()
    subMenu(accountNumber)

def print_statement(accountNumber):
    account=str(accountNumber)
    account="b_"+account
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    start=raw_input("Enter start date : ")
    end=raw_input("Enter the end date : ")
    query="select * from "+account+" where time between :1 and :2"
    cur.execute(query,(start,end))
    print tabulate(cur.description[0])
    print tabulate(cur.fetchall())
    con.commit()
    con.close()
    subMenu(accountNumber)


def money_transfer():
    pass

def account_closure(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    credit=input("enter money to deposit")
    cur.execute("select * from detail where accountnumber=:name",{'name':accountNumber})
    res=cur.fetchall()
    cur.execute("INSERT INTO closed VALUES (:1,:2,:3,:4,:5)",(res[0][0],res[0][1],res[0][2],res[0][3],res[0][4]))
    cur.execute("delete from detail where accountnumber = :name",{'name':accountNumber})
    con.commit()
    con.close()
    subMenu(accountNumber)

def customer_logout():
    pass

def subMenu(accountNumber):
    #print(type(accountNumber))
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
        money_transfer(accountNumber)
    elif(num==6):
        account_closure(accountNumber)
    elif(num==7):
        customer_logout()

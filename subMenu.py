import cx_Oracle
import time
from tabulate import tabulate
import Menu

def address_change(accountNumber):
    print(type(accountNumber))
    new_addr1=raw_input("Enter the new Address Line 1 : ")
    new_addr2=raw_input("Enter the new Address Line 2 : ")
    city=raw_input("Enter city : ")
    state=raw_input("Enter state : ")
    try:
        pin=input("Enter pincode : ")
    except ValueError:
        subMenu(accountNumber)
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    cur.execute("update detail set add1=:1 where accountnumber=:2",(new_addr1,accountNumber))
    cur.execute("update detail set add2=:1 where accountnumber=:2",(new_addr2,accountNumber))
    cur.execute("update detail set city=:1 where accountnumber=:2",(city,accountNumber))
    cur.execute("update detail set state=:1 where accountnumber=:2",(state,accountNumber))
    cur.execute("update detail set pincode=:1 where accountnumber=:2",(pin,accountNumber))
    print("Address Changed Successfully")
    con.commit()
    con.close()
    subMenu(accountNumber)

def money_deposit(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    credit=input("Enter money to deposit")
    if(credit<0):
        print("Invalid amount")
        money_deposit(accountNumber)
    accntNumber=input("Enter the account number : ")
    cur.execute("select * from detail where ACCOUNTNUMBER = :name",{'name':accntNumber})
    if(not(not(cur.fetchall()))):
        cur.execute("update detail set money=money + :1 where accountnumber=:2",(credit,accntNumber))
        cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accntNumber})
        balance=cur.fetchall()
        account=str(accntNumber)
        account="b_"+account
        date=time.strftime("%x")
        query="Insert into "+ account + " VALUES (:1,:2,:3,:4)"
        cur.execute(query,(date,'credit',credit,balance[0][0]))
        print("Balance for "+account+" is "+(str(balance[0][0])))
        con.commit()
        con.close()
        subMenu(accountNumber)
    print("Invalid Account")
    subMenu(accountNumber)


def money_withdraw(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    debit=input("Enter money to withdraw : ")
    cur.execute("select * from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
    if(not(not(cur.fetchall()))):
        cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
        balance=cur.fetchall()
        if(debit>=balance[0][0]):
            print("\nAmount Exceeded !!\n")
            money_withdraw(accountNumber)
        cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
        typ=cur.fetchall()
        if(typ=='ca' or typ=='CA'):
            if((balance-debit)<5000):
                print("\ntransaction fail !! \n")
                money_withdraw(accountNumber)
        cur.execute("update detail set money=money - :1 where accountnumber=:2",(debit,accountNumber))
        cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
        balance=cur.fetchall()
        account=str(accountNumber)
        account="b_"+account
        date=time.strftime("%x")
        query="Insert into "+ account + " VALUES (:1,:2,:3,:4)"
        cur.execute(query,(date,'debit',debit,balance[0][0]))
        print("Balance for "+str(accountNumber)+" is "+(str(balance[0][0])))
        con.commit()
        con.close()
        subMenu(accountNumber)
    print("Invalid Account number")
    subMenu(accountNumber)

def print_statement(accountNumber):
    account=str(accountNumber)
    account="b_"+account
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    start=raw_input("Enter start date (mm/dd/yy) : ")
    end=raw_input("Enter the end date (mm/dd/yy) : ")
    if(start>=end):
        print("\nDate Error !!\n")
        print_statement(accountNumber);
    query="select * from "+account+" where time between :1 and :2"
    cur.execute(query,(start,end))
    print tabulate(cur.fetchall())
    con.commit()
    con.close()
    subMenu(accountNumber)


def money_transfer(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    accntNumber=input("Enter the account number of reciever : ")
    amnt=input("Enter money to Transfer : ")
    cur.execute("select * from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
    balance=cur.fetchall()
    if(balance[0][9]<amnt):
        print("\nInsufficient balance !!!\n")
        subMenu(accountNumber)
    if(balance[0][1]=='ca' or balance[0][1]=='CA'):
        if((balance[0][9]-amnt)<5000):
            print("\nCannot Process !!!\n")
            subMenu(accountNumber)
    cur.execute("select * from detail where ACCOUNTNUMBER = :name",{'name':accntNumber})
    if(not(not(cur.fetchall()))):
        cur.execute("update detail set money=money - :1 where accountnumber=:2",(amnt,accountNumber))
        cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accountNumber})
        balance=cur.fetchall()
        account=str(accountNumber)
        account="b_"+account
        date=time.strftime("%x")
        query="Insert into "+ account + " VALUES (:1,:2,:3,:4)"
        cur.execute(query,(date,'debit',amnt,balance[0][0]))
        print("Balance for "+str(accountNumber)+" is "+(str(balance[0][0])))
        cur.execute("update detail set money=money + :1 where accountnumber=:2",(amnt,accntNumber))
        cur.execute("select money from detail where ACCOUNTNUMBER = :name",{'name':accntNumber})
        balance=cur.fetchall()
        account=str(accntNumber)
        account="b_"+account
        date=time.strftime("%x")
        query="Insert into "+ account + " VALUES (:1,:2,:3,:4)"
        cur.execute(query,(date,'debit',amnt,balance[0][0]))
        print("Balance for "+str(accntNumber)+" is "+(str(balance[0][0])))
        con.commit()
        con.close()
        subMenu(accountNumber)
    print("\nNo account exists !!!\n")
    subMenu(accountNumber)


def account_closure(accountNumber):
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    cur.execute("select * from detail where accountnumber=:name",{'name':accountNumber})
    res=cur.fetchall()
    close='close'
    cur.execute("INSERT into closed VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)",(res[0][0],res[0][1],res[0][2],res[0][3],res[0][4],res[0][5],res[0][6],res[0][7],res[0][8],res[0][9],close))
    cur.execute("delete from detail where accountnumber=:name",{'name':accountNumber})
    cur.execute("delete from valid where ID=:name",{'name':accountNumber})
    print("\nAccount number : "+str(accountNumber)+" closed !!\n")
    con.commit()
    con.close()
    subMenu(accountNumber)

def customer_logout():
    Menu.main()

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
        money_transfer(accountNumber)
    elif(num==6):
        account_closure(accountNumber)
    elif(num==7):
        customer_logout()

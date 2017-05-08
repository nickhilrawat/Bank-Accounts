import cx_Oracle
import getNum

def sign_up():
    password=raw_input("Enter the password:")
    l=len(password)
    while l > 8:
        print("Invalid Password:")
        pas=raw_input("Enter the password:")
        l=len(password)
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    accountNumber=getNum.getNum()
    cur.execute ("INSERT INTO valid VALUES (:1,:2)",(accountNumber,password))
    print(accountNumber)
    #print tabulate(cur.fetchall())
    name=raw_input("Enter the name:")
    address=raw_input("Enter the address:")
    money=input("Enter the money to be deposited at the start:")
    cur.execute("INSERT into detail VALUES(:1,:2,:3,:4,:5)",(accountNumber,name,address,money,'open'))
    accountNumber=str(accountNumber)
    accountNumber="b_"+accountNumber
    query="create table "+ accountNumber + " (time date,transact_type varchar2(15),amount int,balance int)"
    cur.execute(query)
    con.commit()
    con.close()

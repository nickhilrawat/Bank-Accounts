import cx_Oracle
import getNum,Menu

def sign_up():
    password=raw_input("Enter the password:")
    l=len(password)
    while l > 8:
        print("Invalid Password:")
        pas=raw_input("Enter the password:")
        l=len(password)

    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()

    typ=raw_input("Enter account type : ")
    while(typ!='ca' and typ!='CA' and typ!='sb' and typ!='SB'):
        typ=raw_input("Enter account type : ")
    fname=raw_input("Enter the Firstname : ")
    lname=raw_input("Enter the Lastname : ")
    add1=raw_input("Address Line 1 : ")
    add2=raw_input("Address Line 2 : ")
    city=raw_input("City : ")
    state=raw_input("State : ")
    try:
        pincode=input("pincode : ")
    except NameError:
        print("Invalid Input")
        Menu.main()
    money=input("Enter the money to be deposited at the start:")

    if(typ=='CA' or typ=='ca'):
        if(money<5000):
            while(money<5000):
                print("You need minimum 5000")
                money=input("Enter the money to be deposited at the start : ")

    accountNumber=getNum.getNum()
    try:
        cur.execute ("INSERT INTO valid VALUES (:1,:2)",(accountNumber,password))
        print(accountNumber)
        cur.execute("INSERT into detail VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)",(accountNumber,typ,fname,lname,add1,add2,city,state,pincode,money,'open'))
        accountNumber=str(accountNumber)
        accountNumber="b_"+accountNumber
        query="create table "+ accountNumber + " (time varchar2(10),transact_type varchar2(15),amount int,balance int)"
        cur.execute(query)
        con.commit()
        con.close()
    except cx_Oracle.DatabaseError as e:
        print("DatabaseError")
        Menu.main()

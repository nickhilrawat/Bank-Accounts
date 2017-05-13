import cx_Oracle
import getNum,Menu,getpass

def sign_up():
    try:
        password=getpass.getpass("Enter the password : ")
        l=len(password)
        while (l<=7):
            print("Invalid Password : ")
            password=getpass.getpass("Enter the password : ")
            l=len(password)

        con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
        cur=con.cursor()

        typ=raw_input("Enter account type SB/CA : ")
        while(typ!='ca' and typ!='CA' and typ!='sb' and typ!='SB'):
            typ=raw_input("Enter account type : ")
        fname=raw_input("Enter the Firstname : ")
        lname=raw_input("Enter the Lastname : ")
        add1=raw_input("Address Line 1 : ")
        add2=raw_input("Address Line 2 : ")
        city=raw_input("City : ")
        state=raw_input("State : ")
    except cx_Oracle.DatabaseError as e:
        print("Datebase Error")
        Main.menu()
    try:
        pincode=input("pincode : ")
    except Exception:
        print("\nInvalid Pincode!!!\n")
        Menu.main()
    if(len(str(pincode))!=6):
        print("\nInvalid pincode !!!\n")
        Menu.main()
    try:
        money=input("Enter the money to be deposited at the start : ")
        while (money<0):
            print("\nInvalid amount!!\n")
            money=input("Enter the money to be deposited at the start : ")
    except Exception:
        print("\nInvalid Money!!\n")
        Menu.main()
    if(typ=='CA' or typ=='ca'):
        if(money<5000):
            while(money<5000):
                print("\nYou need minimum 5000 !!\n")
                money=input("Enter the money to be deposited at the start : ")

    accountNumber=getNum.getNum()
    try:
        cur.execute ("INSERT INTO valid VALUES (:1,:2)",(accountNumber,password))

        cur.execute("INSERT into detail VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)",(accountNumber,typ,fname,lname,add1,add2,city,state,pincode,money,'open'))
        accountNumber=str(accountNumber)
        accountNumber="b_"+accountNumber
        query="create table "+ accountNumber + " (time varchar2(10),transact_type varchar2(15),amount int,balance int)"
        cur.execute(query)
        con.commit()
        con.close()
    except cx_Oracle.DatabaseError as e:
        print("DatabaseError 2")
        Menu.main()
    print(accountNumber)

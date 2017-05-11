import cx_Oracle
from tabulate import tabulate
import getNum
import SignIn,SignUp,subMenu,Menu


def admin_sign_in():
    print("Admin Login")
    try:
        user=raw_input("Enter username")
        pas=raw_input("Password")
        entry=user+"/"+pas+"@localhost/xe"
        con=cx_Oracle.connect(entry)
        cur=con.cursor()
        query="select * from closed"
        cur.execute(query)
        res=cur.fetchall()
        if(not(not(res))):
            print tabulate(res)
            con.commit()
            con.close()
            main()
        print("No Records")
    except cx_Oracle.DatabaseError as e:
        print("Invalid Input")
        Menu.main()

def main():
    num=0
    while num!=4:
          print("Menu\n1.SignUp\n2.SignIn\n3.Admin Login\n4.Sign Out\n")
          num=input("Choose the action:")
          if(num>4):
              main()
          menu = { 1 : SignUp.sign_up,
                   2 : SignIn.sign_in,
                   3 : admin_sign_in,
                   4 : sign_out,
                 }
          menu[num]()

def sign_out():
    print("Thanks for using our Banking Application!!!! ")
    exit()

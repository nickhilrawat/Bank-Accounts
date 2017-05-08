import cx_Oracle
import subMenu

def sign_in():
    accountNumber=raw_input("Enter your account number :")
    password=raw_input("Password")
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    cur.execute("select * from valid where ID=:name",{'name':accountNumber})
    res=cur.fetchall()
    if(res):
        accnt=res[0][0]
        pas=res[0][1]
        if(password==pas):
            print("\nYou have Successfully Logged in !!!\n")
            print(accnt)
            subMenu.subMenu(accnt)
        else:
            print("\nInvalid credentials\nTry Again!!!")
            sign_in()
    else:
        print("\nInvalid credentials\nTry Again!!!")
        sign_in()

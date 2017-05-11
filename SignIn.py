import cx_Oracle
import subMenu,Menu

def sign_in():
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    b=3
    while b>0 :
        try:
            accountNumber=raw_input("Enter your account number :")
            password=raw_input("Password")

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
                    b=b-1
            else:
                print("\nInvalid credentials\nTry Again!!!")
                b=b-1
        except cx_Oracle.DatabaseError as e:
            print("DatabaseError")
            Menu.main()

    cur.execute("select * from valid where ID=:name",{'name':accountNumber})
    res=cur.fetchall()
    if(res):
        cur.execute("delete from detail where accountnumber = :name",{'name':accountNumber})
        cur.execute("delete from valid where ID = :name",{'name':accountNumber})
        con.commit()
        con.close()
    print("\nAccount locked !!\n")

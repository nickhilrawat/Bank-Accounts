
"""
Created on Thu May 11 02:25:16 2017
@author: Nickhil
"""

import cx_Oracle
from random import randint
from tabulate import tabulate
import getNum
import SignIn,SignUp,subMenu

def admin_sign_in():
    print("Admin Login")
    user=raw_input("Enter Username : ")
    pas=raw_input("Password : ")
    entry=user+"/"+pas+"@localhost/xe"
    con=cx_Oracle.connect(entry)
    cur=con.cursor()
    query="select * from closed"
    cur.execute(query)
    print tabulate(cur.fetchall())
    con.commit()
    con.close()

#elif num==4:
def sign_out():
    print("Thanks for using our Banking Application!!!! ")
    exit()
num=0
while num!=4:
      print("Menu\n1.SignUp\n2.SignIn\n3.Admin Login\n4.Sign Out\n")
      num=input("Choose the action:")
      menu = { 1 : SignUp.sign_up,
               2 : SignIn.sign_in,
               3 : admin_sign_in,
               4 : sign_out,
             }
      menu[num]()

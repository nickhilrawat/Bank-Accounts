# -*- coding: utf-8 -*-
"""
Created on Sun May 07 14:25:16 2017

@author: Tanya
"""

import cx_Oracle
from random import randint
from tabulate import tabulate
print("Menu\n1.SignUp\n2.SignIn\n3.Admin Login\n4.Sign Out\n")
num=input("Choose the action:")
n=10
#if num==1:
def sign_up():
    password=raw_input("Enter the password:")
    l=len(password)
    while l >8:
        print("Invalid Password:")
        password=raw_input("Enter the password:")
        l=len(password)
    con=cx_Oracle.connect('NIKHIL/nikhil@localhost/xe')
    cur=con.cursor()
    range_start = 10**(n-1)
    range_end = (10**n)-1
    accountNumber = randint(range_start, range_end)
    cur.execute('INSERT into valid VALUES(:1,:2)',(accountNumber,password))
    cur.execute("SELECT ID FROM (SELECT valid.*,ROWNUM FROM valid ORDER BY ROWNUM DESC) WHERE ROWNUM=1")
    print tabulate(cur.fetchall())
    con.commit()
    con.close()
#elif num==2:
def sign_in():
    submenu = { 1 : sign_up,
                2 : sign_in,
                3 : admin_sign_in,
                4 : sign_out,
              }

    submenu[num]()

#elif num==3:
def admin_sign_in():
    pass

#elif num==4:
def sign_out():
    pass

#else:
    #print("Invalid Choice:")
menu = { 1 : sign_up,
         2 : sign_in,
         3 : admin_sign_in,
         4 : sign_out,
}

menu[num]()

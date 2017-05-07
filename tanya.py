# -*- coding: utf-8 -*-
"""
Created on Sun May 07 14:25:16 2017

@author: Tanya
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 07 14:25:16 2017
@author: Tanya
"""

import cx_Oracle
from random import randint
from tabulate import tabulate

n=10
#if num==1:
def sign_up():
    password=raw_input("Enter the password:")
    l=len(password)
    while l >8:
        print("Invalid Password:")
        password=raw_input("Enter the password:")
        l=len(password)
    con=cx_Oracle.connect('Nikhil/nikhil@localhost/xe')
    cur=con.cursor()
    #range_start = 10**(n-1)
    #range_end = (10**n)-1
    #accountNumber = randint(range_start, range_end)
    accountNumber=3476381095
    cur.execute('INSERT into valid VALUES(:1,:2)',(accountNumber,password))
    cur.execute("SELECT ID FROM (SELECT valid.*,ROWNUM FROM valid ORDER BY ROWNUM DESC) WHERE ROWNUM=1")
    print tabulate(cur.fetchall())
    name=raw_input("Enter the name:")
    address=raw_input("Enter the address:")
    money=input("Enter the money to be deposited at the start:")
    cur.execute("INSERT into detail VALUES(:1,:2,:3,:4,:5)",(accountNumber,name,address,money,'open'))
    con.commit()
    con.close()
#elif num==2:
def sign_in():
    def address_change():
        pass
    def money_deposit():
        pass
    def money_withdraw():
        pass
    def print_statement():
        pass
    def money_transfer():
        pass
    def account_closure():
        pass
    def customer_logout():
        pass
    submenu = { 1 : address_change,
                2 : money_deposit,
                3 : money_withdraw,
                4 : print_statement,
                5 : money_transfer,
                6 : account_closure,
                7 : customer_logout,
               }

    submenu[num]()


#elif num==3:
def admin_sign_in():
    print("Admin Login")

#elif num==4:
def sign_out():
    print("Thanks for using our Banking Application!!!! ")
    exit()

num=0
while num!=4:
      print("Menu\n1.SignUp\n2.SignIn\n3.Admin Login\n4.Sign Out\n")
      num=input("Choose the action:")
      menu = { 1 : sign_up,
               2 : sign_in,
               3 : admin_sign_in,
               4 : sign_out,
             }

      menu[num]()

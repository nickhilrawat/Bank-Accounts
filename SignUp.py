# -*- coding: utf-8 -*-
"""
Created on Sat May 06 23:12:06 2017

@author: Tanya
"""

import cx_Oracle
class SignUP:
    custid=1000000000000000
    password=raw_input("Enter the password")
    l=len(password)
    if l>8:
        print("Enter valid 8 digit password with alphanumeric values allowed")
    name=raw_input("Enter the name:")
    address=("Enter the address:")
    money=("Enter the amount deposited in start:")
    accnt_status='open'
    con=cx_Oracle.connect('TANYA/tanya@localhost/xe')
    cur=con.cursor()
    cur.execute('INSERT into valid VALUES(:1,:2)',(custid,password))
    con.commit()
    con.close()




#first_name=raw_input("Enter the first name:")
#last_name=raw_input("Enter the last name")
#add_line1=raw_input("Enter the address Line 1:")
#add_line2=raw_input("Enter the address Line 2:")
#city=raw_input("City:")
#state=raw_input("State:")
#pincode=input("Enter the pin:")
#phone=input("Enter the Phone Number:")
#email=raw_input("Enter the email:")
#username=raw_input("Enter username:")
#password=raw_input("Enter password:")
#accnt_type=raw_input("Enter the account type:")
#accnt_status=raw_input("Enter the account status:")
#custid=
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cx_Oracle
con=cx_Oracle.connect('NIKHIL/nikhil@localhost/xe')
name1=raw_input("Enter Name:")
address1=raw_input("Enter Address:")
city1=raw_input("Enter City:")
cur=con.cursor()
cur.execute("""CREATE TABLE customer(
           name VARCHAR2(20),
           address VARCHAR2(50),
           city VARCHAR2(15)
           )""")
cur.execute('INSERT into customer VALUES(:1,:2,:3)',(name1,address1,city1))
con.commit()
con.close()
import cx_Oracle
from tabulate import tabulate
con = cx_Oracle.connect('NIKHIL/nikhil@localhost/xe')
cur=con.cursor();
print("Enter the name of Customer")
n=raw_input()
print("Enter salary ")
m=raw_input()
m=int(m)
cur.execute("insert into supplier (supplierid, salary) values (%s,%d)",(n,m))
print("here")

cur.execute("select * from supplier")
print tabulate(cur.fetchall())
print(cur.rowcount)
con.close()

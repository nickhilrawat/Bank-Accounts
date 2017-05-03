import cx_Oracle

con = cx_Oracle.connect('NIKHIL/nikhil@localhost/xe')
print(con.version)
print("here")

con.close()

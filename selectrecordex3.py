import cx_Oracle
con=cx_Oracle.connect("system/Nandu123@localhost/XE")
cur=con.cursor()
cur.execute("select * from Nandu")
rec=cur.fetchall()
for record in rec:
    for val in record:
        print("\t{}".format(val),end="")
    print()
print("_"*20)
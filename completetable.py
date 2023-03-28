#complete table
import cx_Oracle
con=cx_Oracle.connect("system/Nandu123@localhost/XE")
cur=con.cursor()
cur.execute("select * from Nandu")
for cname in [colname[0] for colname in cur.description]:
    print("\t{}".format(cname),end="")
print()
rec=cur.fetchall()
for it in rec:
    for record in it:
        print("\t{}".format(record),end="")
    print()
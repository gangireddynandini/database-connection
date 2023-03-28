import cx_Oracle
con=cx_Oracle.connect("system/Nandu123@localhost/XE")
cur=con.cursor()
cur.execute("select * from Nandu")
colnames1=cur.description
print("_"*30)
for colnames in colnames1:
    print(colnames[0],end="\t")
print()
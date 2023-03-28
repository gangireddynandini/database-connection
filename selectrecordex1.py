import cx_Oracle

con=cx_Oracle.connect("system/Nandu123@localhost/XE")
cur=con.cursor()
cur.execute("select * from Nandu")
print("_"*30)
print("display records")
while(True):
    rec=cur.fetchone()
    if(rec!=None):
        for val in rec:
            print("\t{}".format(val),end="")
        print()
    else:
        print("_"*30)
        break

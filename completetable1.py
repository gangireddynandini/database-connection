import cx_Oracle
try:
    con=cx_Oracle.connect("system/Nandu123@localhost/XE")
    cur=con.cursor()
    tablen=input("enter table name:")
    cur.execute("select * from %s"%tablen)
    #display col names
    print("_"*30)
    for cname in [colname[0] for colname in cur.description]:
        print("\t{}".format(cname),end="")
    print()
    #display record
    rec=cur.fetchall()
    for records in rec:
        for item in records:
            print("\t{}".format(item),end="")
        print()
    print("_"*30)
except cx_Oracle.DatabaseError as db:
    print("prblm in datbase",db)
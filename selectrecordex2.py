import cx_Oracle
def selectrecords():
    con=cx_Oracle.connect("system/Nandu123@localhost/XE")
    cur=con.cursor()
    cur.execute("select * from Nandu order by name desc")
    rec=cur.fetchmany()
    if(rec!=None):
        print("records are")
        print("_"*30)
        for record in rec:
            for val in record:
                print("{} ".format(val) ,end="")
            print()
        else:
            print("\nrec are cmplyt")
selectrecords()

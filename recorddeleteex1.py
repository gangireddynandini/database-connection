import cx_Oracle,sys
def deletere():
    while(True):
        try:
            con=cx_Oracle.connect("system/Nandu123@localhost/XE")
            cur=con.cursor()
            print("_"*30)
            #accept employe num from keyboard
            empno=int(input("enter emp number for deleting rec:"))
            cur.execute("delete from nandu where eno=%d"% empno)
            con.commit()
            if (cur.rowcount>0):
                print("{} rec delete successfully".format(cur.rowcount))
            else:
                print("no record found")
            ch=input("do u wnat to delete one more record:")
            if(ch.lower()=="no"):
                print("thnx for using this prfrm")
                sys.exit()

        except cx_Oracle.DatabaseError as d:
            print(d)
deletere()

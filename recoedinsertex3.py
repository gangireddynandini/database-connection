import cx_Oracle,sys
def insertrecord():
    while(True):
        try:
            con=cx_Oracle.connect("system/Nandu123@localhost/XE")
            cur=con.cursor()
            print("_"*20)
            #accept employe details from keyboard
            eno=int(input("enter emp no:"))
            ename=input("enter name of emp:")
            sal=int(input("enter salary:"))
            cname=input("enter company name:")
            iq="insert into nandu values(%d,'%s',%f,'%s')"
            cur.execute(iq % (eno,ename,sal,cname))
            con.commit()
            print("_"*20)
            print("{} record inserted successfully in employe table".format(cur.rowcount))

            ch=input("do u want to add one more record:")
            if(ch.lower()=="no"):
                print("thnx for using this prgrm")
                sys.exit()
            print("_"*20)
        except cx_Oracle.DatabaseError as db:
            print("prblm in databse")
insertrecord()



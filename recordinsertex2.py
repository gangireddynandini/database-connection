import cx_Oracle,sys
def dd():
    while(True):
        try:
            con=cx_Oracle.connect(user="system",password="Nandu123")
            cur=con.cursor()
            eno=int(input('enter the employee number:'))
            name=input("enter the emplyee name:")
            sal=int(input("enter the salary:"))
            cname=(input("enter ur company name:"))
            q="insert into nandu values(%d,'%s',%d,'%s')"
            cur.execute(q %(eno,name,sal,cname))
            con.commit()
            ch=input("do u want one more record(yes/no):")
            if (ch.lower()=="no"):
                print("thanks for u")
                sys.exit()
        except cx_Oracle.DatabaseError as b:
            print("problem in database:",b)


dd()
import cx_Oracle
def alterwithmodify():
    try:
        con=cx_Oracle.connect("system/Nandu123@localhost/XE")
        cur=con.cursor()
        aq="alter table employe1 modify(eno number(4),name varchar2(30))"
        cur.execute(aq)
        print("employe table altered")

    except cx_Oracle.DatabaseError as db:
        print("prblm in database")
alterwithmodify()
import cx_Oracle
def tablecreate():
    try:
        con=cx_Oracle.connect("system/Nandu123@localhost/XE")
        cur=con.cursor()
        ctq="create table employe2(eno number(2) primary key,name varchar2(10) not null,sal number(5,2) not null)"
        print("employee table created successfully")
        iq = "insert into employe1 values(6,'swetha',35.000)"



        cur.execute(iq)

        con.commit()
        print("record successfully inserted into emp table")
    except cx_Oracle.DatabaseError as B:
        print("prblm in database:",B)
tablecreate()

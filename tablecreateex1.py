import cx_Oracle
def tablecreate():
    try:
        con=cx_Oracle.connect("system/Nandu123@localhost/XE")
        cur=con.cursor()
        ctq="create table nandu(eno number(2) primary key,name varchar2(10) not null,sal number(5,2) not null)"
        print("employee table created successfully")
        al="alter table nandu modify(name varchar2(20))"
        cur.execute(al)
        con.commit()
        print("altered successfully")
    except cx_Oracle.DatabaseError:

        print("prblm in database:")
tablecreate()

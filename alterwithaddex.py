import cx_Oracle
def alterwithadd():
    try:
        con=cx_Oracle.connect("system/Nandu123@localhost/XE")
        cur=con.cursor()
        up="update nandu set name='sree' where eno=7"
        cur.execute(up)
        con.commit()
    except cx_Oracle.DatabaseError as db:
        print("prblm in database:",db)
alterwithadd()

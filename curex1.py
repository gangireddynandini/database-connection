import cx_Oracle
try:
    con=cx_Oracle.connect("system/Nandu123@localhost/XE")
    print("\n type of con=",type(con))
    print("python program obtains connection from db")
    cur=con.cursor()
    print("\n type of cur",type(cur))
    print("cursor obj created")
except cx_Oracle.DatabaseError as db:
    print(db)
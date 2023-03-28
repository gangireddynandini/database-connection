import cx_Oracle,sys
def deleterecord():
    while (True):
        try:
            con=cx_Oracle.connect("system/Nandu123@localhost/XE")
            cur=con.cursor()


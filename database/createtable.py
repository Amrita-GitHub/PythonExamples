import cx_Oracle

con = cx_Oracle.connect("hr","hr","localhost/miner1212")
cursor = con.cursor()
cursor.execute("create table login(username number primary key not null,password  varchar2(20))")
cursor.close()
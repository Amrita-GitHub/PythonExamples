import cx_Oracle
#dsn = cx_Oracle.makedsn('localhost','1521', service_name="miner1212")
dsn = cx_Oracle.makedsn('localhost','1521', sid="miner1212")
conn = cx_Oracle.connect(user='hr',password='hr', dsn=dsn)
c = conn.cursor()
c.execute('SELECT * FROM departments order by 1')
for row in c: print(row)
conn.close()
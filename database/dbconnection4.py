import cx_Oracle
#Net Service Names for Connection Strings
# tnsnames.ora
#name can be used directly for the data source name parameter dsn of cx_Oracle.connect() and cx_Oracle.SessionPool()
tnsora ='''(DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = miner1212)
    )
  )'''

conn = cx_Oracle.connect("hr","hr",tnsora)
c = conn.cursor()
c.execute('SELECT * FROM departments')
for row in c: print(row)
conn.close()

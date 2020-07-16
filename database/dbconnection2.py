import cx_Oracle

#[username/[password]@]host[:port][/instance_name][?param1=value1&...&paramN=valueN]
conn = cx_Oracle.connect("hr/hr@localhost:1521/miner1212")
c = conn.cursor()
c.execute('SELECT * FROM departments')
for row in c: print(row)
conn.close()
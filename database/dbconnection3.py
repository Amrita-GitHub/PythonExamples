import cx_Oracle

#https://cx-oracle.readthedocs.io/en/latest/user_guide/connection_handling.html
# use with statement to enable autoclosing,
# ensures that a connection is closed once the block is completed

with cx_Oracle.connect("hr/hr@localhost:1521/miner1212") as conn:
    cursor = conn.cursor()
    cursor.execute("insert into departments values(2,'training',100,1700,'n')")
    conn.commit()

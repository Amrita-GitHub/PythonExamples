import cx_Oracle

# Create the session pool
pool = cx_Oracle.SessionPool("hr", "hr",
        "localhost/miner1212", min=2, max=5, increment=1, encoding="UTF-8")

# Acquire a connection from the pool
connection = pool.acquire()

# Use the pooled connection
cursor = connection.cursor()
for result in cursor.execute("select * from employees"):
    print(result)

# Release the connection to the pool
pool.release(connection)

# Close the pool
pool.close()
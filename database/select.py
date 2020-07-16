import cx_Oracle

con = cx_Oracle.connect("hr","hr","localhost/miner1212")
cursor = con.cursor()

# row = cursor.execute("select * from login  where username= :uname and password = :upass ",uname=102,upass="dinesh")
# for i in row:
#     print(i)


#fectchone() to fetch one row
# row = cursor.execute("select * from login  where username= :uname and password = :upass ",uname=102,upass="dinesh")
# print(row.fetchone())

#fectchone() to fetch all rows
row = cursor.execute("select * from login ")
rows = row.fetchall()
for row in rows:
    print(row)



con.close()

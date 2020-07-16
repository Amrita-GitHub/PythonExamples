import cx_Oracle

con = cx_Oracle.connect("hr","hr","localhost/miner1212")
cursor = con.cursor()
cursor.execute('''insert into departments (department_id,department_name,manager_id,location_id,deleted) 
               values(:did,:dname,:mgrid,:locid,:del)''' ,{'did': 3,'dname':'Research','mgrid':100,'locid':1700,'del':'N'})
cursor.close()
con.commit()
con.close()





import json
emp = '''{"id": 119,
      "FIRST_NAME": "Karen",
      "LAST_NAME": "Colmenares",
      "EMAIL": "KCOLMENA",
      "PHONE_NUMBER": "515.127.4566",
      "HIRE_DATE": "1999-08-10", 
      "SALARY": 2500,
      "DEPARTMENT_ID": 30}'''

x= json.loads(emp)
print(x["EMAIL"])

#convert a json object into python dictionary
print(json.dumps(x))
print(json.dumps(x, indent=20))
#print(json.dumps(x,separators=" : "))
import json


#convert from JSON to Python, returns a dictionary
x =json.load(open("c:/employeeData.json","r"))
print(x)

#convert from python to json

json.dump(x,open("c:/employeeData123.json","w"))
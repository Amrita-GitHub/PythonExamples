name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)

import json
#print(json.dumps(rec))
s= json.dumps(rec) #Serialize obj to a JSON formatted str

o = json.loads(s) #Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object
print(o)

#Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object)
#The json module always produces str objects, not bytes objects. Therefore, fp.write() must support str input.
json.dump(rec, fp=open('../files/testjson.txt', 'w'), indent=4)
print(open('../files/testjson.txt', 'r').read())


#deserialize from file as a python object
p = json.load(open("../files/testjson.txt"))
print(p)
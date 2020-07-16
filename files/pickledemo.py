x,y,z=10,20,30
S="Amrita"
S1= "Saxena"
D={"name":"dinesh", "age":45 }
L=['a','e','i','o','u']

Fw = open("pickledatafile.txt","wb")
import pickle
pickle.dump(x,Fw)
pickle.dump(D,Fw)

Fw.close()

Fr = open("pickledatafile.txt","rb")
print(pickle.load(Fr))
print(pickle.load(Fr))


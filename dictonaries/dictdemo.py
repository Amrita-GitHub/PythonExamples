D = {'spam': '2', 'ham': 1, 'eggs': 3}
print(len(D))
print(D)
print(D.get("spam")) #fetches value based on key
print(D.get("toast")) #A key that is missing, return None
print(D.get("toast",88))
print(D["ham"]) #fetches value based on key
print("ham" in D) #Membership: key present test
print(D.keys()) #retrieves all keys #Dictionary views (Python 3.X)
print(list(D.keys())) # returns  a list of key
print(D.values()) #retrieves all values
print(list(D.values()))
print(D.items()) #all key+value list of tuples,
D["spam"]="bread" #Adding/changing keys
print(D)
#


D2={"toast": 4, "muffin":5}
D.update(D2)
print(D)
print("*" * 80)


#

d11 = D.popitem()
print(list(d11))  # retrieve the poped item in a list manually
print(d11)  #by default gives the poped item as a tuple
print(D)
print("*" * 80)


D3={"puff": 4}
D.update(D3)
D1 = D.copy() #copies one dict to another dict
print(D)
print(D1)
print("*" * 80)



D.clear() #clear (remove all items),
print(len(D))
print(D)
print("*" * 80)
#

#alternate way of constructing dictionary
D=dict(name="amrita",age=45)
print(D)
print("*" * 80)

#
#alternate way of constructing dictionary
#keywords, key/value pairs, zipped key/value pairs, key lists
D=dict([("name","saxena"),("age",55)])
print(D)
print("*" * 80)
#
# #alternate way of constructing dictionary
# #keywords, key/value pairs, zipped key/value pairs, key lists
keyslist=["name","mathur"]
valuelist=["age",35]
D=dict([keyslist,valuelist])
print(D)
print("*" * 80)
#
#
#aasignment to get the correct value based on the key
for key in D: #no need to call D.keys() to iterate
    print(key, "=>")
print("*" * 80)
#
# #Dictionary Comphresions
#assigment ,manual code for this
D2={x: x*2 for x in range(10)}
print(D2)

#
#Zip
print(list(zip(['a','b','c'],[1,2,3])))
print(dict(zip(['a','b','c'],[1,2,3])))

#
#Zip with comprhension
D4={k:v  for (k,v) in zip(['a','b','c'],[1,2,3])}
print(D4)
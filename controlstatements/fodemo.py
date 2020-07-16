# from itertools import product
#
for x in ["red","green","yellow"]:
     print(x, end="  ")
#
# #compute the sum and product of all the items in a list
#
sum=0
product=1
for i in [1,2,3,4,5]:
    sum = sum + i
    product = product * i
print(sum, end="  ")
print(product, end="  ")
#
# #iterate over string
# name =  "Amrita Saxena"
# for s in name : print(s,end="  ")
#
# #iterate over tuple
# msg = ("i'm, ok")
# for s1 in msg: print(s1,end="  ")
#
#
# for  (a,b) in [(1,1),(2,4),(3,9),(4,16),(5,25)]:
#     print(a,b)
#
# for  both in [(1,1),(2,4),(3,9),(4,16),(5,25)]:
#     print(both)
#
#
# #iterate over dictionarie
#
d={"a": 1, "b" : 2, "c":3}
print(list(d.items()))

for key in d:
    print(key, "=>" , d[key])

for (key,value) in list(d.items()):
    print(key, "=>" , value)
#
#

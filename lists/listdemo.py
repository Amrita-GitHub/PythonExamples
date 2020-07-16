print(3 in [1,2,3,4,5])

print("*" * 80)

for x in [10,30,50]:
    print(x)
print("*" * 80)

for i in (list(range(10))):
    print(i)

print("*" * 80)
#list comprehensions
l=[x**2 for x in range(5)]
print(l)
print("*" * 80)

for d in "saxena":
    print(d*2)
print("*" * 80)


# manual list comprehensions
result=[]
for d in "saxena":
    result.append(d*2)
print(result)

print("*" * 80)

# automatic list comprehensions
res= [d*2 for d in "saxena"]
print(res)
print("*" * 80)





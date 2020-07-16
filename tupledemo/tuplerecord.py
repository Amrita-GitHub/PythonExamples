#Tuple Record

# bob1 = ('Bob', 40.5, ['dev', 'mgr'])
# print(bob1)
#
# print(bob1[2])
# print(bob1[2][1])

#Tuple Record- Accessed as Dictionary

bob2 = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob2)
print(bob2.keys())
print(bob2.values())
print(tuple(bob2.values()))
print(list(bob2.items()))
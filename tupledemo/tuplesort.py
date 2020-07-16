T = ('cc', 'aa', 'dd', 'bb')
print(T)
print("*" *80)

T1 = list(T)
T1.sort()
print(T1)
#
#Generate a tuple from a list
print(tuple(T1))
#
#
print("*" *80)

print(tuple(sorted(T)))
print("*" *80)
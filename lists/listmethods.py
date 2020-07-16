L = ['eat', 'more', 'SPAM!']
L.append("Please")
print(L)
print("*" * 80)

# L.append(str([1,2,3]))
# L.extend(str([1,2,3]))
# print(L)
# print("*" * 80)

L.sort()
print(L)
L.sort(reverse=True)
print(L)
print("*" * 80)

L.sort(key=str.lower)
print(L)
print("*" * 80)
#
#
print(sorted(L))
print("*" * 80)
#
# #convert to lower case iterate through the list and sort
print(sorted(x.lower() for x in L))
print("*" * 80)
#
L.pop(0) # by default, deletes the -1 element from the list, behaves like a stack
print(L)
print("*" * 80)
#
print(list(reversed(L))) #reverses an item and returns as a list
print("*" * 80)
#
print(L.reverse()) # returns None
print(L)
print("*" * 80)
#
#

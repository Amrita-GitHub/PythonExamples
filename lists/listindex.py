# search for an item’s offset-index
# insert an item at an offset (insert)
# remove an item by value (remove)
# count the number of occurrences  (count)


L= ['spam', 'eggs', 'ham']
print(L.index("eggs"))
print("*" * 80)

L.insert(1,"toast")
print(L)
print("*" * 80)

#delete by value
L.remove("eggs")
print(L)
print("*" * 80)


#delete by position
L.pop(0)
print(L)
print("*" * 80)

print(L.count("ham"))
print("*" * 80)

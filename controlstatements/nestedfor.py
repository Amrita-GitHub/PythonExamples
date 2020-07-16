items = ["aaa", 111, (4, 5), 2.01] # A set of objects
tests = [(4, 5), 3.14] # Keys to search for

for key in tests: # For all keys
    for item in items: # For all items
        if item == key: # Check for match
            print(key, "was found")
            break
else:
    print(key, "not found!")

#or use simple code

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found!")


#It performs a typical data-structure task with a for—collecting common items in two sequences (strings)—

seq1="dinesh"
seq2="amrita"
res=[]
for x in seq1:
    if x in seq2:
        res.append(x)
        print(res)

#shortcut with comphersion pattern
print("--------------")
print([x for x in seq1 if x in seq2])



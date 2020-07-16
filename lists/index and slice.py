l=["hello", "Hello", "HELLO"]
print(l[2])
print(l[-2])
print(l[1:])

print("*" * 80)
l[1]= "world"  # replace and insert at offset
print(l)

print("*" * 80)
l[0:2]=["Good","Morning"] # replace/delete and insert a portion
print(l)

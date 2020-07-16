#use this to parrallely execute list of name and address

#l1 # studentid(1,2,3,4,)

#l2 #name(amrita,reet,purnima,X)

l1=(1,2,3,4)
l2=(5,6,7,8)

print(zip(l1,l2)) #must use zip with list in 3.x
print(list(zip(l1,l2)))

print("#------------------------------------------------------------------#")

for (x,y) in zip(l1,l2):
    print((x,y), '=>', (x+y))


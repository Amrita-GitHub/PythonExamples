x,y,z=10,20,30
S="Amrita"
S1= "Saxena"
D={"name":"dinesh", "age":45 }
L=['a','e','i','o','u']
F = open("datafile.txt","w")
F.write("%s %s %s \n" %(x,y,z))
F.write(S + "\n");
F.write(S1+ "\n")
#F.write(D) #cannot write dict directly to file, must be a string only
F.write(str(D)+ "\n")
F.write(str(L) + "\n")
F.close()

fread = open("datafile.txt")
#print(fread.read().split(","))


#convert integers read from first line to int from strings
line= fread.readline().rstrip()
print(line)
parts = line.split(" ")
print(parts)
nums =[int(p) *2 for p in parts]
print(nums)

line2= fread.readline()
print(line2)
line3= fread.readline()
print(line3)

#convert dict from string to object
line4= fread.readline()
print(line4)
print(eval(line4))

line5= fread.readline()
print(line5)
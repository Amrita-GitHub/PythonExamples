input=open(r"D:/ADFClassFlow.txt","r")
output=open(r"D:\PythonADFClassFlow.txt","w")
fileread = input.read(); #uses a builtin iterator to iterate throughthe file
fileread1= input.readline() # reads a single line
fileread2= input.readlines()  #reads the lines along with \n as a list
#print(fileread)

for x in fileread:
    print(x, end= "  ")
    filewrite = output.write(x)
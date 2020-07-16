#input name and age from user, break in case no inpput is given, else print and display the names

while True:
    name=input("Enter name")
    if name == "stop":break
    year = int(input("Enter age"))
    age =  year +1
    if age <=0 :break
    print("Hello", name)
    print("You will be ", age, "..next year")
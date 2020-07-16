colour = ["red","green","blue"]
print(colour)


tuplecolour = ("red","green","blue")
print(tuplecolour)

dictcolor = {1:"red",
             2:"green",
             3:"blue"}
print(dictcolor)
choice = int(input("enter a color of your choice"))
print(choice,  ' ' , dictcolor.get(choice))


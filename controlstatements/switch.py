from itertools import chain

menu={'ham':1.99,
      'eggs':0.99,
      'bread':1.00}
print(menu)

choice=input("Enter your choice of product to purchase")
#print(menu.get(choice))
#print(menu.get(choice,'bad choice')) # default case


#An in membership test in an if statement can have the same default effect:

if choice in menu:
    print(menu[choice])
    # or
    print(menu.get(choice))
else:
    print("bad choice")



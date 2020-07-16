y=int(input("enter a number to calculate the prime"))
x = y // 2 # For some y > 1
while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break # Skip else
    x -= 1
else: # Normal exit
    print(y, 'is prime')



##old way of writing code with loop else
# y=int(input("enter a number to calculate the prime"))
# x = y // 2 # For some y > 1
# found = False
# while x > 1 and not found:
#     if y % x == 0: # Remainder
#         print(y, 'has factor', x)
#         found = True
#     else:
#         x -= 1
# if not found:
#     print(y, 'is prime')
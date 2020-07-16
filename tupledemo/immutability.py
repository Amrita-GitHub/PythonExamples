
# T=(1,2,3)
# print(T)
# T[0]=10
# print(T)


T = (1, [2, 3], 4)
#T[1]="spam" #error encountered
T[1][0] =200  # can modify a list inside a tuple
print(T)

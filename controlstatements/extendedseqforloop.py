for(a,b,c) in [(1,2,3),(4,5,6)]:
    print(a,b,c)

# In Python 3.X, because a sequence can be assigned to a more general set of names with
# a starred name to collect multiple items, we can use the same syntax to extract parts of
# nested sequences in the for loop:

for (a,*b,c) in [(1,2,3,4),(5,6,7,8)]:
    print(a, b, c)

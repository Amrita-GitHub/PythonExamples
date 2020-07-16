def power(x, y=2):
    r = 1
    while y > 0:
        r = r * x
        y = y - 1
    return r


print(power(2, 3))
print(power(3,2))
print(power(y=2,x=5))

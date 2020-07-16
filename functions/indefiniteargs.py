def example_fun(x, y, **other):
    print("x: {0}, y: {1}, keys in 'other': {2}".format(x,y, list(other.keys())))
    other_total = 0
    for k in other.keys():
        other_total = other_total + other[k]
    print("The total of values in 'other' is {0}".format(other_total))

example_fun(2,y="1",foo=3,bar=4)


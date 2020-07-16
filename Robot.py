class Robot:
    pass

x=Robot()
x.name="Marvin"
x.build_year="1979"

print(x)
print(x.__dict__)
print(x.name,  x.build_year)
y=Robot()
y.name="Caliban"
y.build_year='1993"'
print(y)
print(y.__dict__)
print(y.name, y.build_year)




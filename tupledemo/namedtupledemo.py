from collections import namedtuple # Import extension type
MyRec = namedtuple("MyRec",["name","age", "jobs"] ) # Make a generated class
print(MyRec)
Amrita=MyRec("Amrita",45,["Trainer", "Consultant"]) # A named-tuple record
Saxena=MyRec("Saxena",55,["HR", "Consultant"]) # A named-tuple record
print(Amrita)
print(Amrita[1]) # Access by position
print(Amrita.jobs) # Access by attribute
print(Saxena.jobs)

print("*" *80)
for x in Amrita:
    print(x)


print("*" *80)
#Dictionary methods to access NamedTuple
D=Amrita._asdict()
print(D)
print(D["age"])
D
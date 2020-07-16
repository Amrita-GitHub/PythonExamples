class Parent:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

class Child(Parent):

    def __init__(self, name,age):
        Parent.__init__(self,name)
        self.age = age

    def getAge(self):
        return self.age


class GrandChild(Child):

    def __init__(self, name,age,address):
        Child.__init__(self,name,age)
        self.address = address

    def getAddress(self):
        return self.address


gc = GrandChild("Rohan", 20, "Arkansas")
print(gc.getName(), gc.getAge(), gc.getAddress())

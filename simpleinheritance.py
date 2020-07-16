
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name.." ,self.name)
        print("Age..", self.age)

    def isEmployee(self):
         return False


class Employee(Person):
    def isEmployee(self):
        return True


p = Person("Amrita", 45)
p.display()
print(p.isEmployee())

e = Employee("Dinesh", 45)
e.display()
print(e.isEmployee())
#cose to call constuctor and method of super class

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
    def __init__(self, id, name, age, salary):
        Person.__init__(self, name, age)
        self.id = id

        self.salary = salary
        # call  the superclass constructor
        # without this line the error encountered is
        #AttributeError: 'Employee' object has no attribute 'name'


    def display(self):
        print("Id.." ,self.id)
        print("Saalry..", self.salary)
        #call the super class method
        Person.display(self)


    def isEmployee(self):
        return True


p = Person("Amrita", 45)
p.display()
print(p.isEmployee())

e = Employee(1, "Dinesh", 45 ,100000)
e.display()
print(e.isEmployee())
#parent
class Dog:
    #classvar
    species = "mammal"

    #constructor
    def __init__(self, name, age):

        self.name = name
        self.age = age

    #instance method
    def description(self):
         return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self,sound):
        return "{} says {}".format(self.name, sound)

#child
class shiztuz(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,speed)

#child
class Pom(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,speed)


#directly instantiaing a class
#scobby = Dog("scobby", 6)

#using inheritance
scobby= shiztuz("scobby",5)
print(scobby)
print(scobby.description())
print(scobby.speak("Bow Bow"))
print(scobby.run("fast"))

#using inheritance to instantiate a class
fury = Pom("fury", 25)
print(fury)
print(fury.description())
print(fury.speak("Gruf Gruf"))
print(fury.run("slowly"))


#are fury and scobby instances of Dog

print(isinstance(scobby,Dog))
print(isinstance(fury,Dog))


junior = Pom("junior", 10)

print(junior.description())
print(junior.run("fast"))
print(junior.speak("Grrrr...."))
print(isinstance(junior,Dog))
print(isinstance(junior,Pom))
print(isinstance(junior,shiztuz))

#Access the instance attributes

print(" {} is {}".format(scobby.name,  scobby.age ))
print(" {1} is {0}".format(fury.age ,fury.name))

if scobby.species == "mammal":
    print(" {} is   a {}".format(scobby.name, scobby.species))








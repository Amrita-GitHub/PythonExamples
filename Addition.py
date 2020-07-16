class Addition:
    first=0
    second=0
    result=0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def calculate(self):
        self.result = self.first + self.second
        return self.result

    def display(self):
        print("First Number" , self.first)
        print("Second Number", self.second)
        print("Result", self.result)

obj1 = Addition(101,202)
obj1.calculate()
obj1.display()
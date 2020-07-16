class Robot1:



    #constructor
    def __init__(self, rname=None, build_year=None):
        self.rname = rname
        self.build_year = build_year

    def sayhi(self):
        if self.rname:
            print("Hi..I am..", self.rname)
        else:
            print("Hi..I am a robot without any name")

        if self.build_year:
            print("I was built in the year",self.build_year)
        else:
            print("I do not know my build_year")


x = Robot1("Dinesh", 1975)
print(x)
x.sayhi()

y=Robot1()
print(y)
y.sayhi()






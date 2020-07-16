class Shape:

    def __init__(self, d1, d2):
        print("2 arg constructor")
        self.d1 = d1;
        self.d2 = d2;

    def area(self):
        print("area of shape..", 0)


class Circle(Shape):
    def area(self):
        print("area of Circle...", (3.14 * self.d1 * self.d1))


class Rectangle(Shape):
    def area(self):
        print("area of Rectangle...", (self.d1 * self.d2))


class Ball(Circle):

    def area(self):
        super().area() 
        print(" Ball of {} area  is bouncinng" )


#s = Shape(1,2)
#s.area()

c = Circle(2,3)
c.area()

b = Ball(1,1)
b.area()

c1 = Shape(10,20)
c1.area()

r= Rectangle(2,4)
r.area()

r1 = Shape(10,20)
r1.area()
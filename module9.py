class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
import math

# extends
class Circle(Shape):
    def __init__(self, r, x, y):
        super().__init__(x,y)
        self.r = r
    def get_area(self):
        return math.pi*self.r*self.r

class Square(Shape):
    def __init__(self, a, x, y):
        super().__init__(x,y)
        self.a = a
    def get_area(self):
        return self.a*self.a
shapes=[Circle(1,1,2),Square(2,3,10),Circle(3,2,5)]
print(sum(shape.get_area() for shape in shapes))

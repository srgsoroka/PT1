class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#extends
class Circle(Shape):
    pass

c=Circle(2,3)

print(vars(c))
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# extends
class Circle(Shape):
    def __init__(self, r, x, y):
        super().__init__(x,y)
        self.r = r


c = Circle(2, 3)

print(vars(c))

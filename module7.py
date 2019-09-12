class A:
    def __init__(self):
        self.a=1
        self._donttouchme=2
        self.__secret=3

a=A()

print(a.a)

print(a._donttouchme)

print(vars(a))
class A:
    def f(self,x):
        print(self)
        self.x=x

a=A()

print(a)
a.f(42)

print(vars(a))

class B:
    pass

b=B()
A.f(b,32)

print(b.x)
def f(x):
    def g(y):
        return x*y
    return g

double = f(2)

print(double)

m=double(3)
print(m)
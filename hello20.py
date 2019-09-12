def f():
    def g(x):
        return 2 * x

    return g


double = f()
map(double, [1,2,3,4,5])
print(list(map(double, [1,2,3,4,5])))
print(tuple(map(double, [1,2,3,4,5])))
print(map(double, [1,2,3,4,5]))
m=map(double, [1,2,3,4,5])
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))



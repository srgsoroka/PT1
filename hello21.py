import functools


def add(x, y):
    """Add x and y"""
    return x + y


m = functools.reduce(add, [1, 2, 3, 4])

print(m)

m = map(lambda x: 2 * x, [1, 2, 3, 4, 5])
print(m)
m = list(map(lambda x: 2 * x, [1, 2, 3, 4, 5]))
print(m)
f = lambda x:2*x

print(f(2))
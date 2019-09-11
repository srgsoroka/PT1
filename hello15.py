def addmul(x, y):
    return x + y, x * y


a, b = addmul(2, 3)
print(a, b)
print(addmul(12, 13))


def f(x, y=2):
    return x * y


print(f(2))
print(f(2, 3))


def f(a=1, b=2, c=3):
    return a + b + c

print(f())

print(f(2))
print(f(3))

print(f(c=5))

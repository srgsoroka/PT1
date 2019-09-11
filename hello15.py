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

help(f)

print(f(2, c=4))


# error
# f(a=4,2,1)

def add(x, y):
    return x + y


print(add(x=3, y=4))


def f(*args, **kwargs):
    print(args, kwargs)


print(f(1, 2, 3, bbb=3))

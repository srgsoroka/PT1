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

print(sum([1, 2, 3, 4]))


def sum_(*items):
    s = 0
    for item in items:
        s += item
    return s


def f(a, b, c):
    return a + b + c


print(sum_(1, 2, 3, 4))

d = {'a': 1, 'b': 2, 'c': 3}
print(f(**d))

def f(a, l=[]):
    l.append(a)
    print(l)


print(f(1,[2,3]))
print(f(1))

print(f(2))

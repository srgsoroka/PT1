def f(x):
    return 2 * x


print(f(2))

double = f

print(double(3))


def execute(f, x):
    return f(x)


print(execute(double, 23))


def f():
    def g(x):
        return 2 * x

    return g


double = f()
double
print(double(44))

print(f()(44))


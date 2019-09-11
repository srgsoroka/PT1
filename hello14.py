x = 2


def f():
    global x
    x = 3


def f():
    x = 1
    def g():
        nonlocal x
        x = 3

    g()
    print(x)


f()

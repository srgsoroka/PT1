def f():
    x=2
    def g():
        print(x)
    g()
f()
import builtins
print(dir(builtins))
def abs(x):
    return 42
print(abs(-5))
print(builtins.abs(-5))
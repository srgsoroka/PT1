x=1
def f():
    print(x)

f()

def f():
    print(x)
    x=2
f()
#use global
globals()['x']
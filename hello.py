a = 1
try:
    b = 5 / a
    raise ValueError("My message")
except ZeroDivisionError:
    print("ZDE")
except NameError:
    print("NE")
    exit()
except Exception as e:
    print(e)
else:
    print('b=', b)

finally:
    print("Finally")
print("The end")

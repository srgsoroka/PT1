import module1
print(module1.f())
import sys
print(sys.modules)

a=12

print(module1.f())
print(a)
from module1 import a
print(a)

from module1 import *
print(f())

print(module1.f())

import module1 as m1

print(m1.a)
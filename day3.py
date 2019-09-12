obj1={"abc":[1,2,3],123:(3,4,5)}
m=str(obj1)
print(m)

import pickle
s=pickle.dumps(obj1)
print(s)

obj2=pickle.loads(s)
print(obj2)

print(obj1==obj2)

print(obj1 is obj2)
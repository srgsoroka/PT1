#tuple
t=(1,2, 3,2,3)
print(t)
print(type(t))
#dictionary
d={}
print(type(d))
d['a']=1
print(d)
d['b']=2
print(d)
print(d["a"])
d[(1,2,3)]=123
print(d)
for k in d:
    print(k,d[k])
print(d.items())
d.pop((1,2,3))
for key, value in d.items():
    print(key,value)
s="hello"
enumerate(s)
l=list(enumerate(s))
print(l)
for index, value in enumerate(s):
    print(index, value)
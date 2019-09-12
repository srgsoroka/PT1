#infinite cycle
#l=[1,2,3]
#for i in l:
#    l.append(i)
s={1,2,3,1,2}
print(type(s))
print(s)
s1={1,2} | {3,4}
print(s1)
s1={1,2} - {3,4}
print(s1)

s1={1,2} ^ {3,2}
print(s1)

s1={1,2} & {3,2}
print(s1)
print(1 in s1)
print(2 in s1)
l=len({1,2,3,3,3,3,4,4,4})
print(l)
print({1,2} < {3,2})
print({1,2} < {1,2})
#dictionary
d={}
print(type(d))
#set
d=set()
print(type(d))

f=frozenset([1,2,3])
print(type(f))
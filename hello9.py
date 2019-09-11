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
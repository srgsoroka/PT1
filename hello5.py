l=[1,2.3,"abc",True,[1,2,3]]
print(l[0])
print(l)
print(l[1:3])
print(len(l))

l1=[1,2,3]
l2=l1
print(l2)
l1[0]=0
print(l2)
l2=l1[:]
l1[0]=7
print(l1)
print(l2)

l2=l1.copy()
l1[0]=1

print(l1)
print(l2)

l2=l1.copy()
print(l2==l1)
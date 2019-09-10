l=[1,2,3,4,5]
print(dir(l))

l.append(1)

print(l)

print(l.count(1))

print(l.count(7))

l.extend([1,2,3])
print(l)
l.append([1,2,3])
print(l)

print(l.index(1))

print(l.index(1,1))

print(l.index(1,6))

print(l.index(1,7))
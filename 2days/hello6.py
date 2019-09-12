m=[[0]*10]*10
print(m)
m[0][0]=42
print(m)

l=[1,2,3]
m=[2*x for x in l]
print(m)

m=[[0]*10 for _ in range(10)]
m[0][0]=42
print(m)

m=[2*x for x in [1,2,3,4,5] if x%2]
print(m)

m=[x+y for x in [1,2,3] for y in [4,5,6]]
print(m)
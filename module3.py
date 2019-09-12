config = 'json'
a = 123
if config == 'json':
    import json as serializer
elif config == 'pickle':
    import pickle as serializer
m = serializer.dumps(a)
print(m)
import sys

print(sys.path)

sys.path.insert(1,"/tmp")
print(sys.path)

if __name__ == '__main__':
    print("Module started")
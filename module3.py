config='json'
a=123
if config == 'json':
    import json as serializer
elif config=='pickle':
    import pickle as serializer
m=serializer.dumps(a)
print(m)
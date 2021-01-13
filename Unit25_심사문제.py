keys=input().split()
values=map(int, input().split())
x=dict(zip(keys, values))
x={keys: values for keys, values in x.items() if keys!='delta'}
x={keys: values for keys, values in x.items() if values!=30}
print(x)
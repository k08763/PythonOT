a,b=map(int, input().split())
c=[2**i for i in range(b+1) if a<=i<=b]
c.pop(1)
c.pop(-2)
print(c)
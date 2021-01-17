def prime_number_generator(start,stop):
    for n in range(start,stop):
        is_prime=True    #소수 여부를 저장할 변수
        for i in range(2,n-1):
            if n%i==0:
                is_prime=False
        if is_prime==True:
            yield n

start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
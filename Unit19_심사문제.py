x=int(input())
for i in range(x):
    for j in range(x):
        if j+1 < x-i:
            print(' ', end='')
        else:
            print('*', end='')
    for k in range(x-1):
        if k < i:
            print('*', end='')
    print()
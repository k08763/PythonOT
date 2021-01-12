c=list(map(int, input().split(';')))
c.sort(reverse=True)
for i in c:
    print('{:>9,}'.format(i))
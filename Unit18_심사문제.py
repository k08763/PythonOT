st, sp = map(int, input().split())
i = st
while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > sp:
        break
    print(i, end=' ')
    i += 1
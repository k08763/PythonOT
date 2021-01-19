import random
i=random.randint(1,100)
print(i)
a=0
while a != i:
    a=int(input('숫자를 입력하시오: '))
    if a < i:
        print('UP')
    elif a > i:
        print('DOWN')
print('RIGHT')
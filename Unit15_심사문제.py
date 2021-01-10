a=int(input()) # a는 7이상
b=9000 #교통카드 잔액
if 7<=a<=12: # and b>=650
    b-=650
elif 13<=a<=18: # and b>=1050
    b-=1050
else: # elif a>=19 and b>=1250
    b-=1250
print(b)

# else:
#     print('잔액부족')
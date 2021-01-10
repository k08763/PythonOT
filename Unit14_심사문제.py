k, e, m, s = map(int, input().split())
if k<0 or k>100 or e<0 or e>100 or m<0 or m>100 or s<0 or s>100:
    print('잘못된 점수')
else:
    if (k+e+m+s)/4>=80:
        print('합격')
    else:
        print('불합격')
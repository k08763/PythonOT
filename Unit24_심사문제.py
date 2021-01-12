import string
x = str(input())
a = []
for i in x:
    a.append(i.translate(x.maketrans('', '',string.punctuation)))
x=''.join(a)
print(x.count('the'))


## 코딩 파악하기
#1: import
#2: 문단을 str로 입력 받음
#3: 빈 리스트 생성
#4,5: 단락 내 '문장부호', '띄어쓰기 공백'을 '띄어쓰기 공백'으로 변환
#6: 띄어쓰기 공백을 단위로 문단 재구성 ?
#7: 특정 단어의 수 세기 
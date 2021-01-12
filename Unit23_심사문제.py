row, col = map(int, input().split()) 
matrix=[]
for i in range(row):
    matrix.append(list(input()))
print()
for i in range(row):
    for j in range(col):
        cnt=0
        if matrix[i][j] == '.':
            for y in range(i-1, i+2):
                for x in range(j-1, j+2):
                    if not (y<0 or x<0 or y>=row or x>=col):
                        if matrix[y][x] == '*':
                            cnt += 1
            matrix[i][j] = cnt
            print(matrix[i][j], end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()


## 코딩 이해
# 1: 행의 수와 열의 수 설정
# 2: 빈 행렬 생성
# 3~5: 각 행 입력
# 6~15: 행렬 재구성: 인근 지뢰 수(cnt) 세기
# 6,7: 재구성된 행렬(m')의 크기
# 8: '지뢰 수'를 위한 변수(cnt) 설정
# 9: 지뢰가 아닌 부분만 수정하도록 조건 부여 (= 지뢰인 부분 그대로 유지)
# 10,11: '인근'의 범위 설정
# 12: 잘못된 인덱스 피하도록 조건 부여
# 13~15: 인근의 지뢰 세기
# 16: m'의 행 재구성 
# 17, 18: else=지뢰인 부분 (=지뢰인 부분 그대로 유지)
# 19: 다음 행으로 이동
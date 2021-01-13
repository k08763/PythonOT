with open('words.txt', 'r') as file:
    for line in file:
        words=line.split() # 공백을 기준으로 분리
        for word in words:
            if 'c' in word: # c가 있음 출력
                print(word.strip(',.'))
import random   # random 함수를 사용하기 위한 random 모듈 import
from operator import itemgetter     # 감염 인구수로 정렬하기 위한 itemgetter 모듈 import

# 사용자가 백신과 적용할 국가를 골랐을 때 사용되는 클래스
class Choice:       
    # 생성자 값으로 사용자가 선택한 백신,국가 번호와 초기 백신 리스트, 국가 리스트들을 설정
    def __init__(self,vaccineNum,nationNum,vaccineList,nationList):
        self.vaccineList = vaccineList          # 초기 백신 리스트
        self.nationList = nationList            # 초기 국가 리스트
        self.count = 0                          # 완치된 국가 갯수
        self.curedInfectee = 0                  # 치료된 감염자 수
        self.curedNation = []                   # 완치된 국가리스트
        self.addtionInfectee = 0                # 라운드마다 추가 된 감염자
    
    # 사용자가 고른 백신과 적용할 국가의 번호를 받아 해당 국가에 백신을 적용하여 감염자 수를 수정해주는 함수
    def cure(self,vaccineNum,nationNum):
        if self.nationList[nationNum][2] == 0:  # 만약 감염자 수가 0인 국가에 백신을 접종하려고 하면 국가의 번호를 랜덤으로 다시 뽑음
            while self.nationList[nationNum][2] == 0:
                nationNum = random.randint(0,4)

        # 선택한 백신, 선택한 나라에 대한 정보를 print하고 백신이 접종된 국가의 감염자 수를 연산함
        print('')
        print(f'선택된 백신: {self.vaccineList[vaccineNum][0]}, 치료율: {self.vaccineList[vaccineNum][1]*100}%')
        print(f'선택된 나라: {self.nationList[nationNum][0]}, 인구수: {self.nationList[nationNum][1]}명, 감염자수: {self.nationList[nationNum][2]}명')
        print('=======================================')

        # 백신이 접종될 때 치료된 감염자 수
        curedInfectee = int(self.nationList[nationNum][2]*self.vaccineList[vaccineNum][1])
        
        # 백신 접종 된 이후 해당 국가의 총 감염자 수
        infectee = self.nationList[nationNum][2] = int(self.nationList[nationNum][2] - curedInfectee)
        
        # 백신을 접종한 총 감염자 수
        self.curedInfectee += curedInfectee

        # 백신 접종 이후 해당 국가의 총 감염자수가 0일 경우
        if infectee == 0:
            self.count += 1             # self.count(완치된 국가 갯수)를 1증가
            self.curedNation.append(self.nationList[nationNum][0])      # self.curedNation(완치된 국가 리스트)에 국가를 추가
            print('완치 된 국가: ',self.nationList[nationNum][0])       # 완치된 국가 출력
            print('')

    # 백신과 국가에 대한 정보를 담고 있는 리스트를 셔플하는 함수
    def shuffle(self):
        random.shuffle(self.vaccineList)        # 백신 리스트 셔플
        random.shuffle(self.nationList)         # 국가 리스트 셔플

    # 라운드마다 감염자를 해당 국가 인구수의 15% 만큼 증가시키는 함수
    def infecteeIncrease(self):
        for i in self.nationList:   
            if i[2] != 0:               # 이미 완치된 국가에 대해서는 적용하지 않음
                i[2] += int(i[1]*0.15)
                self.addtionInfectee += int(i[1]*0.15) 

    # 감염자 수가 인원 수를 넘어서는 국가가 생길 경우 True를 반환하는 함수
    def checkFinished(self):
        for i in self.nationList:
            if i[1] < i[2]:
                return True
                break
        return False
        

    # 백신 투여 후 모든 나라에 대한 정보를 print해주는 함수
    def printResult(self,roundnum):
        print(f'{roundnum}차 백신 투여 후 감염된 나라에 대한 정보')
        print('=======================================')

        # 모든 국가가 완치되었을 시 나라를 출력하지 않고 해당 메시지를 출력
        if len(self.curedNation) == 5:
            print('모든 국가가 완치되었습니다 !!!')

        # 모든 국가가 완치되지 않았을 시 감염된 국가들을 출력
        else:
            for i in self.nationList:
                # 감염자가 0이 아닌 국가들만 출력
                if i[2] != 0:
                    print('감염 국가 : ',i[0],sep='')
                    print('인구수 : ',i[1],'명',sep='')
                    print('감염 인구수 : ',i[2],'명',sep='')
                    print('')
    
    # 최종 스코어를 print 해주는 함수
    def printScore(self):
        print('=======================================')
        print('               최종 결과               ')
        print('=======================================')
        print(f'라운드마다 추가로 감염된 감염자 수: {self.addtionInfectee}명')
        print(f'백신으로 치료된 감염자 수: {self.curedInfectee}명')
        print('백신으로 완치된 국가: ',end='')
       
        # 만약 완치된 국가가 있을 경우에만 완치된 국가리스트 출력
        if self.curedNation:
            for i in self.curedNation:
                # 출력하려는 국가가 리스트의 마지막 요소가 아닐 경우에 계속 한줄에 연결해서 출력
                if self.curedNation.index(i) != len(self.curedNation)-1:
                    print(i,end=' ')
                
                # 출력하려는 국가가 리스트의 마지막 요소일 경우 갯수까지 출력 후 한줄 띄움
                else:
                    print(f"{i}({self.count}개)")
                    print('')
        
        # 완치된 국가가 없으면 없다고 출력한 후 한줄 띄움
        else:
            print('없음')
            print('')
                
        self.nationList.sort(key=itemgetter(2),reverse=True)    # 감염자 수가 높은 순으로 self.nationList를 정렬
        for i in self.nationList:
            print(str(self.nationList.index(i)+1)+'위')
            print('국가 : ',i[0],sep='')
            print('인구수 : ',i[1],'명',sep='')
            print('감염 인구수 : ',i[2],'명',sep='')
            print('')

# 게임의 초기 데이터(백신,국가가 담겨있는 리스트)
vaccineList = [['백신1',0.25],['백신2',0.5],['백신3',1]]
nationList = [['한국',1500,300],['중국',3000,800],['일본',2000,500],['미국',2500,750],['독일',2200,1000]]

choiceNum = 0   # 사용자가 고른 메뉴 번호 

# 사용자가 5번 게임 종료 메뉴를 고르거나 게임을 시작하여 끝내지 않는 이상 게임은 계속 진행된다. 
while choiceNum != 5:
    print('----------------------------------')
    print('         코로나 종식 게임')
    print('----------------------------------')
    print('1. 백신 정보')
    print('2. 감염된 국가 정보')
    print('3. 게임 시작')
    print('4. 게임 종료')
    print('----------------------------------')

    choiceNum = int(input())    # 사용자가 고른 메뉴 번호 

    if choiceNum == 4:
        print('게임을 종료합니다')
        break
    
    # 초기 데이터(백신 리스트) 출력
    elif choiceNum == 1:
        for i in vaccineList:
            print('백신 이름 : ',i[0],sep='')
            print('백신 치료율 : ',int(i[1]*100),'%',sep='')
            print('')
    
    # 초기 데이터(국가 리스트) 출력
    elif choiceNum == 2:
        for i in nationList:
            print('감염 국가 : ',i[0],sep='')
            print('인구수 : ',i[1],'명',sep='')
            print('감염 인구수 : ',i[2],'명',sep='')
            print('')
    
    # 게임 시작
    elif choiceNum == 3:
        print('사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 차례대로 입력하세요')
        vaccineInput,nationInput = input().split()      # 사용자로부터 백신과 국가 번호를 받아서 변수에 저장
        vaccineInput = int(vaccineInput)            # input 값이 모두 string이므로 int값으로 강제 변환
        nationInput = int(nationInput)              # input 값이 모두 string이므로 int값으로 강제 변환

        # 사용자로부터 입력받은 정보(선택한 백신과 국가번호)와 초기 데이터(백신,국가리스트)로 Choice 인스턴스 생성
        choice = Choice(vaccineInput-1,nationInput-1,vaccineList,nationList)    
        
        # 총 5번 라운드가 진행된다. (사용자가 처음 라운드만 백신과 국가번호를 고르면 나머지 라운드는 자동으로 진행됨)
        for i in range(5):
            # 만약 감염자 수가 해당 국가의 인구 수 보다 많아지면 게임을 중단시키고 바로 최종 결과창으로 이동
            if choice.checkFinished():
                print('감염자 수가 인구 수보다 많은 국가가 발생하였습니다. 게임을 중단합니다 !!')
                break
            print(f'★  { i+1}번째 시도 ★')
            choice.shuffle()        # 1라운드 이후 라운드는 모두 자동으로 진행되기 때문에 매 라운드마다 리스트의 데이터들을 섞어준다.
            choice.cure(vaccineInput-1,nationInput-1)       # 사용자가 고른 백신을 선택한 국가에 접종한다.
            choice.printResult(i+1)        # 백신 접종 결과를 출력한다.

            # 마지막 라운드가 끝나고 더 이상 감염자를 증가시키지 않음
            if i != 4:                     
                choice.infecteeIncrease()

        choice.printScore()     # 최종 스코어를 출력한다.
        print('게임 종료!')
        break

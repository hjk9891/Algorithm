#문제 https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=625
import sys
import math
N,M,Q = map(int,input().split())
eating = {} # 딕셔너리 (ID : 위치) 형태로 들어감
ate = [] # 이미 먹은 사람
map_ = [] # 맵 - 이차원배열
for i in range (N+2) : #패딩 떄문에 +2 해서 돌아감. 행부분

    if i == 0 or i == N+1 :
        temp = ['X' for j in range(M+2)] # 첫행과 마지막행은 'X' 로 채움  인덱스가 1부터 시작하게
        map_.append(temp)
    else :
        t = []
        for i in range(M+2) : # 0열과 마지막 열은 'X' 로채움
            if i == 0 or i == M+1 :
                t.append('X')
            else :
                t.append(0)
        map_.append(t)

for i in range(Q) :
    temp = input().split() # 입력을 배열로 받음 temp[0] = OUT or IN , temp[1] = ID 
    best = [0,0,0] # 좌석 안전도가 최대인곳을 넣음 [안전도값, X, Y] 
    if temp[1] in ate : # ID 가 이미 먹은 사람이면 
        if temp[0] == 'In': # 명령이 In 이면 
            print(temp[1],'already ate lunch.')
            continue
        elif temp[0] ==  'Out' : # 명령이 OUT 이면
            print(temp[1],'already left seat.')
            continue    
    if temp[0] == 'Out': # 명령이 out일때 
        if temp[1] in eating: # 만약 ID가 이미 먹고있따면 
            tem = eating[temp[1]] # 딕셔너리에서 그 사람의 위치를 가져오고
            map_[tem[0]][tem[1]] = 0 # 해당 위치를 다시 0으로 바꿔준다
            ate.append(temp[1]) # 먹은 사람 명단에 추가
            del eating[temp[1]] # 먹고있는 사람 딕셔너리 삭제 
            print (temp[1], 'leaves from the seat','(' + str(tem[0]) +',',str(tem[1])+ ')' + '.')
            continue
        elif temp[1] not in eating and temp[1] not in ate : # 먹고 있는 중이 아니고 먹은 사람도 아닐 때
            print(temp[1], "didn't eat lunch.") 
            continue
       
    if temp[0] == 'In' : # 명령이 In 이라면
        if temp[1] in eating : # 이미 먹고있다면
            print(temp[1], 'already seated.')
            continue

        if (not eating) : # 먹고 있는 사람이 아무도 없다면
            eating[temp[1]] = (1,1) # 먹고 있는 사람을 추가 아무도 없다면 1,1에 무조건 앉힘
            map_[1][1] = temp[1] # 차리를 채워줌                
            print(temp[1], 'gets the seat (1, 1).')
            continue

        for j in range(1,N+1) : # 패딩때문에 1부터 N+1 부분만 돈다 행부분
            for k in range(1,M+1):   # 매딩때문에 1 부터 N+1 부분만 돈다 열부분
                if map_[j][k] == 0 :     # 만약 해당 자리가 비었다면
                    if (map_[j+1][k] == 0 or map_[j+1][k] == 'X') and  (map_[j-1][k] == 0 or map_[j-1][k] == 'X')and (map_[j][k+1] == 0 or map_[j][k+1] == 'X') and (map_[j][k-1] == 0 or map_[j][k-1] == 'X') : # 상하좌우가 패딩이거나 0인곳만 찾기
                        if eating : #먹고 있는 사람이 있다면
                            p = 9223372036854775807 #안전거리 최소값
                            for s in eating.keys() : # 먹고 있는 사람들을 하나씩 위치값을 꺼내옴
                                a = math.sqrt(math.pow(eating[s][0] -j ,2) + math.pow(eating[s][1]-k,2)) #안전거리
                                if p > a : # 만약 안전거리 값이 현재 안전거리보다 크다면 교체
                                    p = a
                            if p > best[0] : # 안전거리 값이 최대 안전거리 값보다 크다면 교체
                                best[0] = p # 최대안전거리
                                best[1] = j # X
                                best[2] = k # Y

            if j == N and best[0] > 0 : # 안전거리가 업데이트 됐고 마지막행 마지막 열까지 본 상황 즉 전체맵을 다 돌았을때 앉을 자리 업데이트
                eating[temp[1]] = (best[1],best[2]) # 먹고있는 사람리스트에 해당 ID를 키로 위치를 value로 저장 ID : (x,y) 형태
                map_[best[1]][best[2]] = temp[1] # 해당 위치를 ID 값으로 넣어줌
                print(temp[1], 'gets the seat','('+ str(best[1])+',', str(best[2]) + ')'+'.')
                
                    
            if j == N and temp[1] not in eating: # 마지막 까지 다봤는데 앉을 자리가 없다면 
                print('There are no more seats.')

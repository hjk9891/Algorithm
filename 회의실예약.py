#문제: https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=626

import sys
N,M = map(int, input().split())
room = []
for i in range(N) :
    room.append(input())
room.sort()

dic = {}
for i in range(M) :
    temp = input().split()
    if temp[0] not in dic :
        dic[temp[0]] = []
    dic[temp[0]].append(int(temp[1]))
    dic[temp[0]].append(int(temp[2]))
    dic[temp[0]].sort()


for i in room :
    answer = []
    print('Room' , i+':')
    if i in dic :
        if dic[i][0] == 9 :
            tt = ''
            for j in range(len(dic[i])) :
                if j % 2 != 0 :
                    if j != len(dic[i])-1 :
                        if dic[i][j] == 9 :
                            tt = '09' +'-' + str(dic[i][j+1])
                            answer.append(tt)
                        else:
                            if dic[i][j] != dic[i][j+1] :
                                tt = str(dic[i][j]) +'-' + str(dic[i][j+1])
                                answer.append(tt)
                    else :
                        if dic[i][j] != 18 :
                            tt = str(dic[i][j]) + '-' + '18'
                            answer.append(tt)
        else:
            tt = ''
            dic[i].insert(0,9) 
            for j in range(len(dic[i])) :
                if j % 2 == 0 :
                    if j != len(dic[i])-1 :
                        if dic[i][j] == 9 :
                            tt = '09' +'-' + str(dic[i][j+1])
                            answer.append(tt)
                        else:
                            if dic[i][j] != dic[i][j+1] :
                                tt = str(dic[i][j]) +'-' + str(dic[i][j+1])
                                answer.append(tt)
                    else :
                        if dic[i][j] != 18 :
                            tt = str(dic[i][j]) + '-' + '18'
                            answer.append(tt)
    else :
       print('1 available:')
       print('09-18')
       if i != room[-1] :
            print('-----')
       continue
    if len(answer) != 0 :
        print(str(len(answer)) +' ' + 'available:')
        for _ in answer :
            print(_)
        if i != room[-1] :
            print('-----')
    if len(answer) == 0 :
        print('Not available')
        if i != room[-1] :
            print('-----')

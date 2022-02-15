# 문제 : https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=804
import sys
al =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mes = input()
key_ = list(set([_ for _ in input()] + al))

key = [[] for _ in range(5)]
j = 0
k = 0
for i in key_:
    key[j].append(i)
    k += 1
    if k == 5 :
        j+=1
        k = 0

mess = ''
cont = 0
for i in range(len(mes)) :
    if cont == 2 :
        mess += ' '
        cont = 0
    if i != len(mes) -1 :
        if mes[i] != mes[i+1]:
            mess += mes[i]
        else :
            change = 'X'
            if mes[i] == 'X':
                change = 'Q'
            if cont == 0 :
                mess += mes[i]
                mess += change
                cont = 2
                continue
            if cont == 1 :
                mess += mes[i]
                cont = 2
                continue
    if i == len(mes)-1 :
        if cont == 1 :
            mess += mes[i]
        if cont == 0 :
            mess += mes[i] + 'X'
             
    cont += 1 
answer = ''
for i in mess.split() :
    fir=[[j,k] for j in range(5) for k in range(5) if key[j][k]== i[0]]
    se =[[j,k] for j in range(5) for k in range(5) if key[j][k]== i[1]]
    if fir[0][0] == se[0][0] :
        if fir[0][1] != 4 :
            answer += key[fir[0][0]][fir[0][1]+1]
        elif fir[0][1] == 4 :
            answer += key[fir[0][0]][0]
        if se[0][1] != 4 :
            answer += key[se[0][0]][se[0][1]+1]
        elif se[0][1] == 4 :
            answer += key[se[0][0]][0] 

    elif fir[0][1] == se[0][1] :
        if fir[0][0] != 4 :
            answer += key[fir[0][0]+1][fir[0][1]]
        elif fir[0][0] == 4 :
            answer += key[0][fir[0][1]]
        if se[0][0] != 4 :
            answer += key[se[0][0]+1][se[0][1]]
        elif se[0][0] == 4 :
            answer += key[0][se[0][1]]
    else :
        answer += key[fir[0][0]][se[0][1]] + key[se[0][0]][fir[0][1]]
print(answer)

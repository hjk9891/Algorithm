#문제 : https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=624

import sys
dic = {'-':'0000000','0': '1111110','1' : '0000110', '2': '1011011', '3' : '1001111', '4' : '0100111', '5' : '1101101',
      '6' : '1111101', '7' : '1100110', '8': '1111111', '9' : '1101111'}

      
N = int(input())

for i in range(N) :
    cont =0
    temp = input().split()
    if len(temp[0]) != len(temp[1]):
        if len(temp[0]) < len(temp[1]) :
            for _ in range(len(temp[1]) - len(temp[0])) :
                temp[0] = '-' + temp[0]
                
        elif len(temp[0]) > len(temp[1]) :
            for _ in range(len(temp[0]) - len(temp[1])) :
                temp[1] = '-' + temp[1]
               
   
    for z in range(len(temp[0])):     
        if dic[temp[0][z]] != dic[temp[1][z]] :
            for _ in range(len(dic[temp[0][z]])) :
                

                if dic[temp[0][z]][_] != dic[temp[1][z]][_]:
                    cont +=1
    print(cont)

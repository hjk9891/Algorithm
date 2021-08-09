def solution(price, money, count):
    answer = 0
    temp = 1 
    while 1:
        answer += price * temp
        temp +=1
        if temp > count :
            break
    if answer > money:
        answer -= money
    else :
        return 0
    return answer

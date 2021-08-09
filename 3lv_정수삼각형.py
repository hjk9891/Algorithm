def solution(triangle):
    for i in range(1,len(triangle)):
        temp= []
        for j in range(len(triangle[i])):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
                continue
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else :
                a = triangle[i][j] + triangle[i-1][j]
                b = triangle[i][j] + triangle[i-1][j-1]
                if a >= b :
                    triangle[i][j] = a
                else :
                    triangle[i][j] = b 
    return max(triangle[len(triangle)-1])
  #dp 문제 - 전에 계산된 값을 활용하여 효울을 좋게함. 재밌었다.

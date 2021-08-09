import heapq as hq
def solution(scores):
    answer = ''
    stu = [[] for x in scores]
    for i in range(len(scores)) :
        for j in range(len(scores[i])):
            stu[j].append(scores[i][j])
            if i == len(scores) -1 :
                stu[j].sort()
                if stu[j][-1] == scores[j][j]:
                    a = stu[j].pop()
                    if a == stu[j][-1] :
                        stu[j].append(a)
                if stu[j][0] == scores[j][j] :
                    if stu[j][0] != stu[j][1] :
                        stu[j].pop(0)
                avg = sum(stu[j])/len(stu[j])      
                if avg >= 90:
                    answer+= 'A'
                elif avg >= 80:
                    answer += 'B'
                elif avg >= 70 :
                    answer += 'C'
                elif avg >= 50 :
                    answer += 'D'
                else : 
                    answer += 'F'
    return answer

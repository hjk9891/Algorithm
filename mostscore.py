def solution(answers):
  ans=[]
  ans.append([1,2,3,4,5]* 2000) #1번학생이 찍은수
  ans.append([2,1,2,3,2,4,2,5] * 1250) # 2번학생 찍은수
  ans.append([3,3,1,1,2,2,4,4,5,5] * 1000) # 3번학생 찍은 수
  
  count = [0,0,0] # 누가 가장 많이 맞춰는가
  
  for i in range(3):
    for j in range(len(answers)):
        if ans[i][j] == answer[j]:
          count[i] += 1
  
  answer = []
  for i in range(3):
    if count[i] == max(count):
      answer.append(i + 1 )
      
  return answer

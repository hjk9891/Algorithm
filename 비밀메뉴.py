#문제 : https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=623
import sys

input_ = input().split()
M = input_[0]
N = input_[1]
K = input_[2]

secret = "".join(input().split())
lis_ = "".join(input().split())

if lis_.find(secret) != -1 :
    print('secret')
else:
    print('normal')

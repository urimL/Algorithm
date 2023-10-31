import sys
from itertools import combinations
input = sys.stdin.readline


n=int(input())
nums = list(map(int,input().split()))
answer = 0

for i in nums:
    if i==1:
        continue
    tmp = True
    for j in range(2,i):
        if i%j==0:
            tmp = False
            break

    if tmp:
        answer+=1

print(answer)

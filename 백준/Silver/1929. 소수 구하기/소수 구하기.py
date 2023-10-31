import sys
from itertools import combinations
input = sys.stdin.readline


n,m = map(int,input().split())
answer = 0

for i in range(n,m+1):
    if i==1:
        continue
    tmp = True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            tmp = False
            break

    if tmp:
        print(i)

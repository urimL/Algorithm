import sys
from collections import deque
input = sys.stdin.readline


n,k = map(int,input().split())
check = [True]*(n+1)
answer=0

for i in range(2,n+1):
  
    for j in range(i,n+1,i):
        if check[j]:
            check[j]=False
            answer+=1


            if answer==k:
                print(j)
                break

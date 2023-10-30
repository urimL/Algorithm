import sys
from itertools import product
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
visited = [False]*n

tmp = []
answer = []

def dfs():
    if len(tmp)==m:
            answer.append(tmp[:])
            return
        
    for i in range(len(arr)):
        if not visited[i] and (not tmp or tmp[-1]<=arr[i]):
            tmp.append(arr[i])
            visited[i]=True
            dfs()
            visited[i]=False
            tmp.pop()

dfs()
answer = sorted(list(set(map(tuple,answer))))

for i in answer:
    for j in i:
        print(j,end=' ')
    print()

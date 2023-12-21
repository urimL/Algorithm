import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
order = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    tmp = list(map(int,input().split()))
    for t in range(1,tmp[0]):
        order[tmp[t]].append(tmp[t+1])
        degree[tmp[t+1]]+=1

result = []
q = deque()

for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)

while q:
    now = q.popleft()

    result.append(now)

    for x in order[now]:
        degree[x] -= 1
        if degree[x]==0:
            q.append(x)

if len(result) != n:
    result = [0]

print(*result,sep='\n')
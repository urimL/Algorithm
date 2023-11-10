import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
answer = [0]*(n+1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x]=True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                answer[i]+=1
                
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)

for i in range(1,n+1):
    visited = [False]*(n+1)
    bfs(i)

max_value = max(answer)
for i in range(1,n+1):
    if answer[i]==max_value:
        print(i,end=' ')

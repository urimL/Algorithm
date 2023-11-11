import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

def dfs(start):
    visited[start]=True
    print(start,end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    visited[start] = True
    q = deque([start])

    while q:
        now = q.popleft()
        print(now,end=' ')

        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                q.append(i)



for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()

visited = [False]*(n+1)    
dfs(v)
print()
visited = [False]*(n+1)    
bfs(v)

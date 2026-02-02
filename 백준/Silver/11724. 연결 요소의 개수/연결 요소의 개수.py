import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = 0

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    

def bfs(t):
    q = deque([t])
    visited[t] = True

    while q:
        now = q.popleft()
        
        for x in graph[now]:
            if not visited[x]:
                q.append(x)
                visited[x] = True

for i in range(1, n+1):
    if not visited[i]:
        bfs(i) 
        answer += 1

print(answer)
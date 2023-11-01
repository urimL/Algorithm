import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

def bfs(graph,start):
    cnt = [0]*(n+1)
    visited = [start]
    q = deque()
    q.append(start)

    while q:
        a = q.popleft()
        for i in graph[a]:
            if i not in visited:
                cnt[i]=cnt[a]+1
                visited.append(i)
                q.append(i)
    return sum(cnt)
    

#양방향 그래프
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1,n+1):
    result.append(bfs(graph,i))

print(result.index(min(result))+1)

import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [False]*(n+1)

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

answer = 0
graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        answer+=1

print(answer)

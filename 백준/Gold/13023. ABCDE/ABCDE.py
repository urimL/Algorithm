import sys
from collections import deque
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [False]*n
arrive = False

def dfs(start,depth):
    global arrive
    if depth==5:
        arrive=True
        return

    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i,depth+1)
            
    visited[start]=False


answer = 0

for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n):
    dfs(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)

import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
road = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
answer = []

def bfs(start):
    q = deque()
    q.append(start)
    visited[start]+=1

    while q:
        now = q.popleft()
        for i in road[now]:
            if visited[i]==-1:
                visited[i] = visited[now]+1
                q.append(i)
                
                if visited[i]==k:
                    answer.append(i)


for i in range(m):
    s,e = map(int,input().split())
    road[s].append(e)

bfs(x)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)

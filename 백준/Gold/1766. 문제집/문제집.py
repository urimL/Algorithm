import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for i in range(m):
    v,e = map(int,input().split())
    graph[v].append(e)
    degree[e] += 1

q = []
for i in range(1,n+1):
    if degree[i] == 0:
        heapq.heappush(q,i)

answer = []
while q:
    now = heapq.heappop(q)
    answer.append(now)

    for x in graph[now]:
        degree[x] -= 1
        if degree[x] == 0:
            heapq.heappush(q,x)


print(*answer)
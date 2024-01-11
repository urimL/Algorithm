import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited = [False] * (n + 1)
visited[1] = True

for i in graph[1]:
    if not visited[i]:
        answer += 1
        visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            answer += 1

print(answer)

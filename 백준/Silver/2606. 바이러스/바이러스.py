import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
count = 0


def dfs(now):
    global count
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            count += 1
            dfs(i)


for i in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

dfs(1)
print(count)

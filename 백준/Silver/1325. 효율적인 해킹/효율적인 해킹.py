import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
answer = []


def bfs(now):
    q = deque()
    q.append(now)
    visited = [False] * (n + 1)
    visited[now] = True
    count = 1

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                count += 1
                q.append(i)

    return count


max_v = 1
for i in range(m):
    v, e = map(int, input().split())
    graph[e].append(v)

for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > max_v:
        max_v = cnt
        answer.clear()
        answer.append(i)
    elif cnt == max_v:
        answer.append(i)

print(*answer)

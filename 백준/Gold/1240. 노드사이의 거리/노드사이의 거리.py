import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])


def bfs(x, y):
    visited[x] = True
    q = deque()
    q.append([x, 0])

    while q:
        now, weight = q.popleft()

        if now == y:
            return weight

        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append([i[0], weight + i[1]])
    return -1


want = [list(map(int, input().split())) for _ in range(m)]
for w in want:
    visited = [False] * (n + 1)
    s, e = w
    count = bfs(s, e)
    print(count)

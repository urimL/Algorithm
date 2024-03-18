import sys
from collections import deque

input = sys.stdin.readline

# 2660
n = int(input())
graph = [[] for _ in range(n + 1)]

while True:
    x, y = map(int, input().split())
    if x == y == -1:
        break
    else:
        graph[x].append(y)
        graph[y].append(x)


def bfs(x):
    q = deque([x])
    cnt = [0] * (n + 1)

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                cnt[i] = cnt[now] + 1
                q.append(i)
                visited[i] = True

    return max(cnt)


result = [100] * (n + 1)
for a in range(1, n+1):
    visited = [False] * (n + 1)
    visited[a] = True
    count = bfs(a)
    result[a] = count

score = min(result)
c = 0
answer = []
for i in range(len(result)):
    if result[i] == score:
        answer.append(i)
        c += 1
        
print(score, c)
print(*answer)

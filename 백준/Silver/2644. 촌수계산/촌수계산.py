import sys

input = sys.stdin.readline

n = int(input())
a,b = map(int, input().split())
r = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer = []


def dfs(now, count):
    visited[now] = True
    if now == b:
        answer.append(count)

    for i in r[now]:
        if not visited[i]:
            dfs(i, count + 1)


m = int(input())
for _ in range(m):
    p, c = map(int, input().split())
    r[p].append(c)
    r[c].append(p)


dfs(a, 0)

if len(answer) == 0:
    print(-1)
else:
    print(answer[-1])
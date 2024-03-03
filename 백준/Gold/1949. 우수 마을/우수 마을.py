import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dp = [[0, 0] for _ in range(n + 1)]
visited = [False] * (n + 1)


def dfs(x):
    visited[x] = True

    dp[x][1] += people[x - 1]
    for c in graph[x]:
        if not visited[c]:
            dfs(c)
            # x가 우수마을이 아닐 경우, c는 우수마을이거나 아닐 수 있다.
            dp[x][0] += max(dp[c][0], dp[c][1])
            # x가 우수마을인 경우, c가 우수마을이 아니다.
            dp[x][1] += dp[c][0]


dfs(1)
print(max(dp[1]))
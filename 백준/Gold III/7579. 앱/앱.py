import sys

# 7579
input = sys.stdin.readline

n, k = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[0] * (sum(c) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(0, sum(c) + 1):
        if j < c[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c[i - 1]] + m[i - 1])

for i, j in enumerate(dp[n]):
    if j >= k:
        print(i)
        break

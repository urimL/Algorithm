import sys

# 1535
input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
pleasure = list(map(int, input().split()))
dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(101):
        h, p = hp[i - 1], pleasure[i - 1]
        if j < h:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - h] + p)

print(dp[n][99])

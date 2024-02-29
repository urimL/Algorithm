import sys

# 1082
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
m = int(input())

dp = [-5001 for _ in range(m + 1)]

for i in range(n - 1, -1, -1):
    now = p[i]
    for j in range(now, m + 1):
        dp[j] = max(i, dp[j - now] * 10 + i, dp[j])

print(dp[m])

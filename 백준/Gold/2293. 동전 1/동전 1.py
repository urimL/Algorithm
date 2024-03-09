import sys

input = sys.stdin.readline

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (m + 1)
dp[0] = 1

coins.sort()
for c in coins:
    for i in range(c,m+1):
        dp[i] += dp[i-c]

print(dp[-1])
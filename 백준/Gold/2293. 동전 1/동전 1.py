import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
coin = []
dp = [0]*(m+1)
dp[0] = 1

for i in range(n):
    coin.append(int(input()))
coin.sort()

for c in coin:
    for i in range(c,m+1):
        dp[i] += dp[i-c]

print(dp[m])
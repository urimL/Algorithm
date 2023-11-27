import sys

input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[1] = 1
tmp = []

for i in range(2,n+1):
    idx = int(i**(0.5))**2

    if idx == i:
        tmp.append(i)
        dp[i] = 1
        continue

    dp[i] = dp[i] = dp[idx]+dp[i-idx]
    for j in tmp:
        dp[i] = min(dp[j]+dp[i-j],dp[i])

print(dp[n])
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]
dp = [1] * (n + 1)

if n > 1:
    dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
if m > 0:
    pos = 0
    for i in range(m):
        answer *= dp[vips[i] - pos - 1]
        pos = vips[i]
    answer *= dp[n-pos]

else:
    answer = dp[n]

print(answer)

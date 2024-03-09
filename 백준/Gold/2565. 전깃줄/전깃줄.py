import sys

input = sys.stdin.readline

n = int(input())
light = [list(map(int, input().split())) for _ in range(n)]
light.sort()
dp = [0] * (n + 1)
for i in range(len(light)):
    for j in range(i):
        if light[i][0] > light[j][0] and light[i][1] > light[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(min(len(light) - max(dp) - 1, n + 1))
